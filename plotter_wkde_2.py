#!/usr/bin/env python
import itertools
import matplotlib as mpl
from matplotlib.pyplot import cm
import pylab as plt
import time
import numpy as np
import pickle

from scipy.interpolate import RegularGridInterpolator

with open('./output/sig_psi_E/pdf/sig_psi_E.pkl', 'rb') as ifile:
    spatial_KDE = pickle.load(ifile)

bins_logsigma = spatial_KDE['bins'][0]
bins_logpsi = spatial_KDE['bins'][1]
bins_logEr = spatial_KDE['bins'][2]

with open('./output/sig_E/pdf/sig_E.pkl', 'rb') as ifile:
    norm_KDE = pickle.load(ifile)
spatial_KDE_vals = spatial_KDE['pdf_vals']/norm_KDE['pdf_vals'][:,np.newaxis,:]

spatial_pdf = RegularGridInterpolator((bins_logsigma, bins_logpsi, bins_logEr),
                                            spatial_KDE_vals,
                                            method='linear', bounds_error=False, fill_value=1.e-20)

import logging
mpl_logger = logging.getLogger('matplotlib')
mpl_logger.setLevel(logging.WARNING)

import rootpy.plotting.root2matplotlib as rplt
from rootpy import plotting
from rootpy.plotting import Hist, Hist2D

from scipy.interpolate import interp1d
from scipy.integrate import quad

plotting.set_style('ATLAS', mpl=True)
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['Verdana']

plt.style.use('ggplot')


mc = np.load('/home/ge56lag/Data/dataset_8yr_fit_IC86_2012_16_MC_2017_09_29_more_fields.npy')

def make_plot(logE, sigma_p, delta_sigma=0.2, show_quantile=False):
    gamma=2.0
    sin_dec = np.sin(np.radians(5.693))
    delta_sin_dec = 0.2
    delta_sigma_p = delta_sigma * sigma_p
    delta_logerec = 0.2

    weights = mc['orig_OW'] * mc['trueE']**(-gamma)
    psi_max = 8.0*sigma_p # for plotting
    idx_erec = np.logical_and(mc['logE']>logE-delta_logerec, mc['logE']<logE+delta_logerec)
    sp = mc['sigma_pull_corrected']/np.pi*180. # degrees
    idx_sigma_p = np.logical_and(sp>sigma_p-delta_sigma_p, sp<sigma_p+delta_sigma_p)

    idx_sin_dec = np.logical_and(np.sin(mc['trueDec'])>sin_dec-delta_sin_dec, np.sin(mc['trueDec'])<sin_dec+delta_sin_dec)
    idx = idx_erec&idx_sin_dec&idx_sigma_p

    selected_psi = mc['psi'][idx]/np.pi*180.
    selected_paraboloid = mc['sigma_pull_corrected'][idx]/np.pi*180. # degrees
    selected_weights = weights[idx]
    selected_energies = mc['logE'][idx]

    print "found",len(mc[idx]),"matching events."
    idx_missing = mc['psi']/np.pi*180>psi_max
    print len(mc[idx&idx_missing]), "events, or", len(mc[idx&idx_missing])*1.0/len(mc[idx]), "% are out of plotting range"
    idx_missing = mc['psi']/np.pi*180>2*psi_max
    print len(mc[idx&idx_missing]), "events, or", len(mc[idx&idx_missing])*1.0/len(mc[idx]), "% are out of histogram bounds"

    idx_missing = selected_psi>2*psi_max
    if len(selected_psi[idx_missing])>0:
        print sorted(selected_psi[idx_missing].tolist())[::-1]

    def eval_kde(logPsi, logE, sigma_p):
        sig_rad = np.radians(sigma_p)
        nbins = len(logPsi)
        return spatial_pdf(np.stack([np.full(nbins, np.log10(sig_rad)),
                                   logPsi, np.full(nbins, logE)], axis=1))

    def eval_kde_weighted(xvals, take_indices):
        xvals_rad = np.radians(xvals)
        xvals_log = np.log10(xvals_rad)
        sumw = np.sum(selected_weights[take_indices])
        yvals_pdf = np.zeros(len(xvals_rad))
        for i in take_indices:
            yvals_pdf += selected_weights[i]/sumw * eval_kde(xvals_log, selected_energies[i], selected_paraboloid[i])
        return yvals_pdf / (xvals_rad*np.log(10)) * np.pi/180.

    def rl_p(x, sigma):
        sigma_sq = sigma**2
        return x/sigma_sq * np.exp(-x**2/(2*sigma_sq))

    def rl_p_weighted(x, take_indices):
        selected_paraboloid
        selected_weights
        sumw = 0
        for idx in take_indices:
            sumw+=selected_weights[idx]
        vals = [selected_weights[i]/sumw * rl_p(x, selected_paraboloid[i]) for i in take_indices]
        return np.sum(vals)

    xvals = np.linspace(1.e-10, psi_max, 1000)
    #xvals_rad = np.radians(xvals)
    #xvals_log = np.log10(xvals_rad)
    #yvals_pdf = eval_kde(xvals_log, logE, sigma_p) / (xvals_rad*np.log(10)) * np.pi/180.


    nterms_max = int(1.e3)
    all_indices = np.array(range(len(selected_weights)))
    if len(all_indices)>nterms_max:
        take_indices = np.random.choice(all_indices, nterms_max, replace=False, p=selected_weights/np.sum(selected_weights))
    else:
        take_indices = all_indices

    yvals_p = np.asarray([rl_p_weighted(tx, take_indices) for tx in xvals])
    yvals_pdf = eval_kde_weighted(xvals, take_indices)


    def get_expected_quantile(fractions=[0.5]):
        xvals = np.linspace(0, 10*np.average(selected_paraboloid, weights=selected_weights), 10000)
        dx = xvals[1]-xvals[0]
        yvals = [rl_p_weighted(x, take_indices) for x in xvals]
        yvals_cdf = [0.0]
        xvals_cdf = [0.0]
        val = 0
        for i in range(len(yvals)-1):
            j=i+1
            val+=yvals[j]*dx
            yvals_cdf.append(val)

        # strip duplicate values
        yvals_stripped = []
        xvals_stripped = []
        for i in range(len(yvals)-1):
            if yvals_cdf[i+1]>yvals_cdf[i]:
                yvals_stripped.append(yvals_cdf[i])
                xvals_stripped.append(xvals[i])

        xvals_stripped.append(xvals[-1])
        yvals_stripped.append(1.0)

        inv_cdf = interp1d(yvals_stripped, xvals_stripped, kind=5)
        return np.array([inv_cdf(frac) for frac in fractions])


    #fracs = [0.1 + i * 0.2 for i in range(5)]
    #percs = get_expected_quantile(fractions=fracs)

    bins=np.linspace(0,2*psi_max,80)
    hist = Hist(bins)
    hist.Sumw2()
    hist.fill_array(selected_psi, weights[idx])
    hist.Scale(1./hist.Integral("width"))
    hist.title="MC simulation"
    plt.plot(xvals, yvals_p, 'r-', label="paraboloid")
    rplt.errorbar(hist, markersize=0, elinewidth=2)
    #plt.plot(xvals, yvals_p, 'r-', label="paraboloid")
    plt.plot(xvals, yvals_pdf, 'g-', label="KDE PDF")
    plt.xlabel('$\Psi\,|\,Erec, sin\delta, \sigma_p\,\,\,\,[deg]$', fontsize=20)
    plt.ylabel('pdf', fontsize=20)
    plt.xlim([0.0, psi_max])
    #plt.plot([-1,-2],[-1,-1],'k--', label='quantiles (0.1-0.9)')
    plt.ylim(ymin=0)
    plt.title("$log_{10}E/GeV=%.1f,\,\\sigma_p=%.2f,\,\\Delta\\sigma_p/\\sigma_p=%.2f$" %(logE, sigma_p, delta_sigma))

    ax = plt.axes()
    #colors=cm.magma(np.linspace(0.2,0.8,len(fracs)))
    #ax.vlines(percs, 0, 1, transform=ax.get_xaxis_transform(), colors=colors, linestyle='dashed')
    #ax.vlines(percs, np.zeros(len(fracs)), np.asarray([rl_p_weighted(tx, take_indices) for tx in percs]), colors=colors, linestyle='dashed', linewidth=1)


    for axis in ['top','bottom','left','right']:
              ax.spines[axis].set_linewidth(1.5)
              ax.spines[axis].set_color('0.0')

    ax.tick_params(axis='both', which='both', width=1.5, colors='0.0', labelsize=16)
    ax.yaxis.set_ticks_position('both')
    plt.legend(prop={'size':16})
    ax.xaxis.label.set_color('0.2')
    ax.yaxis.label.set_color('0.2')

    plt.subplots_adjust( hspace=0 )


    plt.savefig("./output/wkde_cpd_rayleigh_lE_%.1f_sigma_%.2f.pdf" %(logE, sigma_p))
    plt.clf()

'''
make_plot(2.0, 0.2)
make_plot(2.0, 0.5)
make_plot(2.0, 1.5)
make_plot(2.5, 0.2)
make_plot(2.5, 0.5)
make_plot(2.5, 1.5)
make_plot(3.0, 0.18)
make_plot(3.0, 0.38)
make_plot(3.0, 1.0)
make_plot(3.5, 0.15)
make_plot(3.5, 0.25)
make_plot(3.5, 0.8)
make_plot(4.0, 0.10)
make_plot(4.0, 0.2)
make_plot(4.0, 0.7)
make_plot(4.5, 0.10)
make_plot(4.5, 0.15)
make_plot(4.5, 0.6)
make_plot(5.0, 0.05)
make_plot(5.0, 0.12)
make_plot(5.0, 0.6)
make_plot(5.5, 0.05)
make_plot(5.5, 0.12)
make_plot(5.5, 0.5)
make_plot(6.0, 0.05)
make_plot(6.0, 0.12)
make_plot(6.0, 0.5)
'''

#make_plot(4.0, 0.13)
make_plot(5.0, 0.15)
#make_plot(5.0, 0.1)
#make_plot(5.5, 0.1)
#make_plot(6.0, 0.1)









