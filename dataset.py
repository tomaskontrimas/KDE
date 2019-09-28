# -*- coding: utf-8 -*-

import numpy as np
from numpy.lib import recfunctions as np_rfn
import os.path

from config import CFG
from functions import assert_file_exists


class Dataset(object):
    """docstring for Dataset"""
    def __init__(self, pathfilenames):
        super(Dataset, self).__init__()
        self.pathfilenames = pathfilenames

        self.mc_field_name_renaming_dict = dict()
        self.data_preparation_functions = list()

    def load_data(self):
        """Loads the data, which is described by the dataset.

        Note: This does not call the ``prepare_data`` method! It only loads
              the data as the method names says.

        Returns
        -------
        data : numpy record ndarray
            A numpy record ndarray holding the monte-carlo data.
        """
        if isinstance(pathfilenames, basestring):
            pathfilenames = [pathfilenames]
        pathfilename = pathfilenames[0]
        assert_file_exists(pathfilename)
        data = np.load(pathfilename)
        for i in range(1, len(pathfilenames)):
            pathfilename = pathfilenames[i]
            assert_file_exists(pathfilename)
            data = np.append(data, np.load(pathfilename))

        return data

    def prepare_data(self, data):
        """Prepares the data by calling the data preparation callback functions
        of this dataset.

        Parameters
        ----------
        data : DatasetData instance
            The DatasetData instance holding the data.
        """
        for data_prep_func in self._data_preparation_functions:
            data_prep_func(data)

    def load_and_prepare_data(pathfilenames):
        """Loads the data file(s), renames fields and applies diffuse dataset cuts.

        Parameters
        ----------
        pathfilenames : str | sequence of str
            The file name(s), including path(s), of the monte-carlo data file(s).

        Returns
        -------
        data : numpy record ndarray
            Loaded and prepared monte-carlo data.
        """
        data = load_data()

        # Rename fields based on MC_keys dictionary.
        data = np_rfn.rename_fields(data, CFG['MC_keys'])

        # Apply diffuse dataset cuts.
        data = diffuse_cuts(data)

        return data

    def add_data_preparation(self, func):
        """Adds the given data preparation function to the dataset.

        Parameters
        ----------
        func : callable
            The object with call signature __call__(data) that will prepare
            the data after it was loaded. The argument 'data' is a DatasetData
            instance holding the experimental and monte-carlo data. The function
            must alter the properties of the DatasetData instance.

        """
        if(not callable(func)):
            raise TypeError('The argument "func" must be a callable object with call signature __call__(data)!')
        self._data_preparation_functions.append(func)

    @property
    def mc_field_name_renaming_dict(self):
        """The dictionary specifying the field names of the monte-carlo data
        which need to get renamed just after loading the data. The dictionary
        values are the new names.
        """
        return self._mc_field_name_renaming_dict
    @mc_field_name_renaming_dict.setter
    def mc_field_name_renaming_dict(self, d):
        if(not isinstance(d, dict)):
            raise TypeError('The mc_field_name_renaming_dict property must '
                'be an instance of dict!')
        self._mc_field_name_renaming_dict = d

    @property
    def data_preparation_functions(self):
        """The list of callback functions that will be called to prepare the
        data (experimental and monte-carlo).
        """
        return self._data_preparation_functions

