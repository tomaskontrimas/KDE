# -*- coding: utf-8 -*-

import numpy as np
import os.path

def assert_file_exists(pathfilename):
    """Checks if the given file exists.

    Parameters
    ----------
    pathfilenames : str
        The file name, including path.

    Raises
    ------
    RuntimeError
        If the file does not exist.
    """
    if(not os.path.isfile(pathfilename)):
        raise RuntimeError('The data file "%s" does not exist!'%(pathfilename))

def diffuse_cuts(mc):
    """Applies diffuse dataset cuts on a given monte-carlo data.

    Parameters
    ----------
    mc : str | numpy record ndarray
        Monte-carlo data.

    Returns
    -------
    mc_dc : numpy record ndarray
        Monte-carlo data after diffuse dataset cuts.
    """
    mc_dc = mc[(mc['true_dec'] > np.radians(-5)) &
               (np.log10(mc['true_energy']) < 8.0) &
               (mc['sigmaok'] == 0)]
    return mc_dc

def great_circle_distance(ra_1, dec_1, ra_2, dec_2):
    '''Computes the great circle distance between two events.

    Parameters
    ----------
    ra_1 : float
        Right ascension of the first event in radians.
    dec_1 : float
        Declination of the first event in radians.
    ra_2 : float
        Right ascension of the second event in radians.
    dec_2 : float
        Declination of the second event in radians.

    Returns
    -------
    gcd : float
        The great circle distance between two events.
    '''
    delta_dec = np.abs(dec_1 - dec_2)
    delta_ra = np.abs(ra_1 - ra_2)
    x = np.sin(delta_dec/2.)**2 + np.cos(dec_1)*\
        np.cos(dec_2)*np.sin(delta_ra/2.)**2
    gcd = 2*np.arcsin(np.sqrt(x))
    return gcd

def powerlaw(energy, phi0=1.01*1e-18, gamma=2.19):
    '''Computes a powerlaw with `phi0` normalization and `gamma` index.

    Parameters
    ----------
    energy : numpy ndarray of floats | float
        Energy.
    phi0 : float
        Powerlaw normalization.
    gamma : float
        Powerlaw index.

    Returns
    -------
    pl : numpy ndarray of floats | float
        Powerlaw with `phi0` normalization and `gamma` index.
    '''
    # pl = phi0*(energy/1.e5)**(-gamma)
    pl = phi0*(energy)**(-gamma)
    return pl

def pl_weighting(mc, phi0, gamma):
    return mc['orig_OW']*powerlaw(mc['true_energy'], phi0=phi0, gamma=gamma)

def conv_weighting(mc, *args):
    return mc['conv']

# Could be wrong!
def conv_pl_weighting(mc, phi0, gamma):
    return conv_weighting(mc) + pl_weighting(mc, phi0, gamma)

def bg_weighting(mc, phi0, gamma):
    return conv_weighting(mc) + mc['astro']

def plotter_wkde_weighting(mc, phi0, gamma):
    return mc['orig_OW']*mc['true_energy']**(-gamma)
