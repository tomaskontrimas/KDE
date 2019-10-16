# -*- coding: utf-8 -*-

import importlib
import itertools
import logging
import numpy as np
import os
from functools import reduce

from sklearn.model_selection import KFold
from scipy.interpolate import RegularGridInterpolator

from .config import CFG
from .dataset import Dataset
from .functions import diffuse_cuts

# ROOT imports.
os.environ["ROOT_INCLUDE_PATH"] = os.pathsep + CFG['paths']['meerkat_root']
from ROOT import gSystem, gStyle, RooRealVar, std, Double
gSystem.Load(CFG['paths']['meerkat_lib'])

from ROOT import (
    OneDimPhaseSpace,
    CombinedPhaseSpace,
    BinnedKernelDensity,
    AdaptiveKernelDensity,
    Logger
)

from root_numpy import array2tree

# Set Meerkat package log level to errors only.
Logger.setLogLevel(2)


class Model(object):
    """The Model class initializes and stores variables based on the provided
    model module and given parameters. It is used for the KDE instance
    generation.
    """
    def __init__(self, model_module, dataset=None, weighting=None, phi0=1.0,
                 gamma=2.0, nbins=None):
        """Creates a new model object.

        Parameters
        ----------
        model_module : str
            Name of model file inside models directory.
        dataset : Dataset, optional
            Instance of `Dataset` class containing Monte-carlo data. If not
            provided the default `IC_mc` dataset from configuration is used.
        weighting : function | str | sequence of floats, optional
            The function is called with `mc`, `phi0` and `gamma` arguments.
            String is looked for in config `weighting_dict`. Sequence of weights
            has to be the same length as the monte-carlo data. If no option is
            given falls back to uniform weighting.
        phi0: float, optional
            Powerlaw normalization, default is 1.0.
        gamma : float, optional
            Powerlaw index, default is 2.0. Supports one decimal point
            precision.
        """
        super(Model, self).__init__()
        self.logger = logging.getLogger('KDE.' + __name__ + '.Model')
        model = importlib.import_module('models.{}'.format(model_module))

        # Choose settings and grid from model.
        str_gamma = '{:.2f}'.format(gamma)
        if str_gamma not in model.settings.keys():
            self.logger.info('Using default model settings and setting gamma '
                'to 2.0.')
            gamma = 2.0
            settings = model.settings['default']
            if model.grid is None:
                grid = None
            else:
                self.logger.info('Using default model grid.')
                grid = model.grid['default']
        else:
            settings = model.settings[str_gamma]
            if model.grid is None:
                grid = None
            elif str_gamma in model.grid.keys():
                grid = model.grid[str_gamma]
            else:
                self.logger.info('Using default model grid.')
                grid = model.grid['default']

        if dataset is None:
            if CFG['paths']['IC_mc'] is not None:
                dataset = Dataset(CFG['paths']['IC_mc'])
                dataset.mc_field_name_renaming_dict(CFG['paths']['MC_keys'])
                dataset.add_data_preparation(diffuse_cuts)

                # mc = load_and_prepare_data(CFG['paths']['IC_mc'])
            else:
                raise ValueError('No suitable dataset provided.')

        mc = dataset.load_and_prepare_data()

        self.values = [eval(settings[key]['values'], None, {'mc': mc})
                       for key in settings]
        self.vars = [key for key in settings]
        self.bandwidth_vars = [key + '_bandwidth' for key in settings]
        if nbins is None:
            self.nbins = [settings[key]['nbins'] for key in settings]
        else:
            self.nbins = [nbins for key in settings]
        self.bandwidths_adaptive = [settings[key]['bandwidth_adaptive'] for key in settings]
        self.bandwidths_binned = [settings[key]['bandwidth_binned'] for key in settings]
        self.ranges = [eval(str(settings[key]['range']))
                       if settings[key]['range'] is not None
                       else [min(self.values[i]), max(self.values[i])]
                       for i, key in enumerate(settings)]
        self.mc = mc
        self.phi0 = phi0*1e-18  # Renormalize in units of 1e-18 1/GeV/cm^2/sr/s.
        self.gamma = gamma

        # Calculate KDE normalization.
        range_norm = [1.0] + [bound[1] - bound[0] for bound in self.ranges]
        self.kde_norm = reduce((lambda x, y : x/y), range_norm)

        self.weighting_dict = CFG['weighting_dict']
        self.weights = self._generate_weights(weighting)

        if grid is None:
            self.out_bins = [np.linspace(self.ranges[i][0], self.ranges[i][1],
                                         self.nbins[i])
                             for i, key in enumerate(settings)]
        else:
            self.out_bins = [grid[key] for key in settings]
        self.coords = np.array(list(itertools.product(*self.out_bins)))

    def _generate_weights(self, weighting):
        """Private method to generate weights by a given option.

        Parameters
        ----------
        weighting : function | str | sequence of floats, optional
            The function is called with `mc`, `phi0` and `gamma` arguments.
            String is looked for in config `weighting_dict`. Sequence of weights
            has to be the same length as the monte-carlo data. If no option is
            given falls back to uniform weighting.

        Returns
        -------
        weights : numpy ndarray of floats
            Generated weights with a given `weighting` option.
        """
        if callable(weighting):
            return weighting(self.mc, self.phi0, self.gamma)
        elif isinstance(weighting, list):
            if len(weighting) != len(self.mc):
                raise ValueError('Weighting list length should be equal to the '
                                 'MC length.')
            return weighting
        elif weighting in self.weighting_dict:
            return self.weighting_dict[weighting](self.mc, self.phi0, self.gamma)
        else:
            self.logger.info('Using ones as weight.')
            return np.ones(len(self.mc))


class KDE(object):
    """The KDE class provides methods for kernel density estimation and cross
    validation.
    """
    def __init__(self, model):
        """Creates a new KDE object.

        Parameters
        ----------
        model : Model
            Instance of `Model` class.
        """
        super(KDE, self).__init__()
        self.logger = logging.getLogger('KDE.' + __name__ + '.KDE')
        self.model = model
        self.binned_kernel = None
        self.adaptive_kernel = None
        self.cv_result_dtype = np.dtype({
            'names': ['bandwidth', 'LLH', 'Zeros'],
            'formats': ['(' + str(len(self.model.vars)) + ',)f4', 'f4', 'f4']
        })

        self._generate_tree_and_space()

    def _generate_tree_and_space(self, index=None):
        """Private method to generate a tree object of the given data with
        weights and a combined phase space over data ranges.

        Parameters
        ----------
        index : numpy ndarray of floats | None
            Indices for selection of the monte-carlo and weights data subset.
        """
        self.tree = None
        spaces = []
        if index is None:
            index = slice(len(self.model.values[0])) # Index the whole array.
        for i, var in enumerate(self.model.vars):
            spaces.append(OneDimPhaseSpace(var, *self.model.ranges[i]))
            if self.tree is None:
                value_array = np.array(self.model.values[i][index], dtype=[(var, np.float32)])
                self.tree = array2tree(value_array)
            else:
                value_array = np.array(self.model.values[i][index], dtype=[(var, np.float32)])
                array2tree(value_array, tree=self.tree)

        array2tree(np.array(self.model.weights[index],
            dtype=[("weight", np.float32)]), tree=self.tree)

        if len(spaces) == 1:
            self.space = spaces[0]
        else:
            self.space = CombinedPhaseSpace("PhspCombined", *spaces)

    def generate_binned_kd(self, bandwidth, pdf_seed=None):
        """Wrapper method of `BinnedKernelDensity` constructor for N-dimensional
        kernel PDF with binned interpolation from the sample of points in an
        NTuple with weight.

        Parameters
        ----------
        bandwidth : list floats
            List of kernel widths.
        pdf_seed : KernelDensity | None
            PDF seed for the approximation PDF.

        Returns
        -------
        binned_kernel : BinnedKernelDensity
            BinnedKernelDensity instance.
        """
        if pdf_seed is None:
            pdf_seed = 0

        args = []
        args.extend([
            "BinnedKernelDensity",
            self.space,  # Phase space.
            self.tree  # Input NTuple.
        ])
        args.extend(self.model.vars)  # Variables to use.
        args.append("weight")  # Weights.
        args.extend(self.model.nbins)  # Numbers of bins.
        args.extend(bandwidth)  # Kernel widths.
        args.extend([pdf_seed,  # Approximation PDF (0 for flat approximation).
                     0])  # Sample size for MC convolution (0 for binned convolution)

        self.binned_kernel = BinnedKernelDensity(*args)

        return self.binned_kernel

    def generate_adaptive_kd(self, bandwidth, pdf_seed=None):
        """Wrapper method of `AdaptiveKernelDensity` constructor for
        N-dimensional adaptive kernel PDF from the sample of points in an NTuple
        with weight.

        Parameters
        ----------
        bandwidth : list floats
            List of kernel widths.
        pdf_seed : KernelDensity | None
            PDF seed for the width scaling and the approximation PDF.

        Returns
        -------
        adaptive_kernel : AdaptiveKernelDensity
            AdaptiveKernelDensity instance.
        """
        # Generate pdf_seed if not provided.
        if pdf_seed is None:
            pdf_seed = self.generate_binned_kd(bandwidth)

        args = []
        args.extend([
            "AdaptiveKernelDensity",
            self.space,  # Phase space.
            self.tree  # Input NTuple.
        ])
        args.extend(self.model.vars)  # Variables to use.
        args.append("weight")  # Weights.
        args.extend(self.model.nbins)  # Numbers of bins.
        args.extend(bandwidth)  # Kernel widths.
        args.extend([pdf_seed,  # PDF for kernel width scaling.
                     pdf_seed,  # Approximation PDF (0 for flat approximation).
                     0])  # Sample size for MC convolution (0 for binned convolution), self.tree.GetEntries()

        self.adaptive_kernel = AdaptiveKernelDensity(*args)

        return self.adaptive_kernel

    def eval_point(self, kernel_density, coord):
        """Evaluates PDF value at a given coordinate of normalized
        `KernelDensity` instance.

        Parameters
        ----------
        kernel_density : KernelDensity
            Binned or adaptive `KernelDensity` instance.
        coord : tuple of floats
            Coordinates of a point at which the `kernel_density` is evaluated.

        Returns
        -------
        value : float
            Evaluated PDF value at a given coordinate of normalized
            `kernel_density`.
        """
        l = len(coord)
        v = std.vector(Double)(l)
        for i in range(l):
            v[i] = coord[i]
        return kernel_density.density(v)*self.model.kde_norm

    def set_kfold_subset(self, n_split):
        """Generates and sets tree and space of `n_split` data subset.

        Parameters
        ----------
        n_split : int
            Number of fold to cross validate.
        Returns
        -------
        validation_index : list(float)
            Validation indices of data subset.
        """

        kfold = KFold(n_splits=CFG['project']['n_splits'],
                      random_state=CFG['project']['random_state'], shuffle=True)

        training_index, validation_index = list(kfold.split(self.model.mc))[n_split]

        self._generate_tree_and_space(training_index)

        return validation_index

    def cross_validate_split(self, bandwidth, n_split, adaptive=False, pdf_seed=None):
        """Calculates average log likelihood value with given bandwidth on a
        dataset using K-Folds cross-validator.

        Parameters
        ----------
        bandwidth : list floats
            List of kernel widths.
        n_split : int
            Number of fold to cross validate.
        adaptive : boolean
            Chooses AdaptiveKernelDensity generator if True and
            BinnedKernelDensity generator if False.
        pdf_seed : KernelDensity | None
            PDF seed for the width scaling and the approximation PDF.

        Returns
        -------
        cv_result_split : numpy record ndarray
            Cross validation array containing bandwidth, log likelihood and
            zeros values.
        """
        validation_index = self.set_kfold_subset(n_split)

        if adaptive:
            kernel_density = self.generate_adaptive_kd(bandwidth, pdf_seed)
        else:
            kernel_density = self.generate_binned_kd(bandwidth, pdf_seed)

        training_pdf_vals = self.get_pdf_values(kernel_density)

        # Validation
        rgi_pdf = RegularGridInterpolator(tuple(self.model.out_bins),
            training_pdf_vals, method='linear', bounds_error=False,
            fill_value=0)

        mc_validation_values = []
        for i, var in enumerate(self.model.vars):
            mc_validation_values.append(
                self.model.values[i][validation_index])

        likelihood = rgi_pdf(list(zip(*mc_validation_values)))
        inds = likelihood > 0.

        weights = self.model.weights[validation_index]
        weights /= np.sum(weights)

        llh = np.sum(np.log(likelihood[inds])*weights[inds])
        zeros = len(likelihood) - len(inds)
        result_tuple = tuple([tuple(bandwidth), llh, zeros])
        cv_result_split = np.array([result_tuple], dtype=self.cv_result_dtype)
        return cv_result_split

    def cross_validate(self, bandwidth, adaptive=False, pdf_seed=None):
        """Calculates average log likelihood value with given bandwidth on a
        dataset using K-Folds cross-validator.

        Parameters
        ----------
        bandwidth : list floats
            List of kernel widths.
        adaptive : boolean
            Chooses AdaptiveKernelDensity generator if True and
            BinnedKernelDensity generator if False.
        pdf_seed : KernelDensity | None
            PDF seed for the width scaling and the approximation PDF.

        Returns
        -------
        cv_result : numpy record ndarray
            Cross validation array containing bandwidth, log likelihood and
            zeros values.
        """
        result = np.array([], dtype=self.cv_result_dtype)
        for n_split in range(CFG['project']['n_splits']):
            cv_result_split = self.cross_validate_split(bandwidth, n_split,
                adaptive=adaptive, pdf_seed=pdf_seed)
            result = np.append(result, cv_result_split)

        result_tuple = tuple([tuple(bandwidth), np.average(result['LLH']),
                              np.average(result['Zeros'])])

        cv_result = np.array([result_tuple], dtype=self.cv_result_dtype)
        return cv_result

    def cross_validate_bandwidths(self, bandwidths=None, adaptive=False,
                                  pdf_seed=None):
        """Calculates average log likelihood value with given bandwidth on a
        dataset using K-Folds cross-validator for given `bandwidths` or
        generated product of the model bandwidth ranges.

        Parameters
        ----------
        bandwidths : list of list floats | None
            List of kernel widths.
        adaptive : boolean
            Chooses AdaptiveKernelDensity generator if True and
            BinnedKernelDensity generator if False.
        pdf_seed : KernelDensity | None
            PDF seed for the width scaling and the approximation PDF.

        Returns
        -------
        cv_results : numpy record ndarray
            Cross validation array containing bandwidths, log likelihoods and
            zeros values.
        """
        cv_results = np.array([], dtype=self.cv_result_dtype)
        if bandwidths is None:
            if adaptive:
                bandwidths = self.model.bandwidths_adaptive
            else:
                bandwidths = self.model.bandwidths_binned

        for bandwidth in itertools.product(*bandwidths):
            self.logger.info('Bandwidth: %s', bandwidth)
            result = self.cross_validate(bandwidth, adaptive)
            cv_results = np.append(cv_results, result)
        return cv_results

    def get_pdf_values(self, kernel_density):
        """Evaluates PDF values at all coordinates of normalized `KernelDensity`
        instance.

        Parameters
        ----------
        kernel_density : KernelDensity
            Binned or adaptive `KernelDensity` instance.

        Returns
        -------
        pdf_values : numpy ndarray of floats
            Evaluated PDF values.
        """
        pdf_values = np.asarray([self.eval_point(kernel_density, coord)
                               for coord in self.model.coords])
        pdf_values = pdf_values.reshape(self.model.nbins)
        return pdf_values
