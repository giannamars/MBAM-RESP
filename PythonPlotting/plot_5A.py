# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:03:41 2018

@author: Gianna
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
plt.rc('text', usetex=False)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)
plt.rc('legend', fontsize=8)
width = 3.487
golden_mean = (np.sqrt(5)-1.0)/2.0   # aethestic ratio
height = width*golden_mean



################################################################################    Reduction 1

dfPhi1=pd.read_csv('Figures/CSV/figure_5a_panel1_param_Phi1.csv', header=None)
dfPhi1.columns = ['eigentime', 'Phi1']
#
dfmR=pd.read_csv('Figures/CSV/figure_5a_panel1_param_mR.csv', header=None)
dfmR.columns = ['eigentime', 'mR']

#
dfr0=pd.read_csv('Figures/CSV/figure_5a_panel1_param_r0.csv', header=None)
dfr0.columns = ['eigentime', 'r0']

#
dfalpha=pd.read_csv('Figures/CSV/figure_5a_panel1_param_muG.csv', header=None)
dfalpha.columns = ['eigentime', 'muG']


fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.13, bottom=.15, right=.99, top=.97)

dfPhi1.plot(x='eigentime', y= 'Phi1', ax=ax1, label=r'$\Phi_1$', color='#252525')
dfmR.plot(x='eigentime', y= 'mR', ax=ax1, label=r'$m_R$', color='#cccccc')
dfr0.plot(x='eigentime', y= 'r0', ax=ax1, label=r'$r_0$', color='#636363')
dfalpha.plot(x='eigentime', y= 'muG', ax=ax1, label=r'$\mu_G$', color= '#969696')

ax1.set_xlabel(r'$\tau$', labelpad=0)
ax1.set_ylabel(r'$\log\,\vartheta$', labelpad=0)

plt.legend(bbox_to_anchor=(0.1, 0.02, 0.4, .502), loc=3,
       ncol=2, mode="expand", borderaxespad=0., frameon=False)

fig.set_size_inches(width, height)
fig.savefig('Resp_5A1.pdf')

################################################################################    Reduction 2

dfPhi2=pd.read_csv('Figures/CSV/figure_5b_panel1_param_Phi2.csv', header=None)
dfPhi2.columns = ['eigentime', 'Phi2']
#
dfPhi3=pd.read_csv('Figures/CSV/figure_5b_panel1_param_Phi3.csv', header=None)
dfPhi3.columns = ['eigentime', 'Phi3']

#
dfPhi4=pd.read_csv('Figures/CSV/figure_5b_panel1_param_muG.csv', header=None)
dfPhi4.columns = ['eigentime', 'muG']



fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.165, bottom=.15, right=.99, top=.97)

dfPhi2.plot(x='eigentime', y= 'Phi2', ax=ax1, label=r'$\Phi_2$', color='#252525')
dfPhi3.plot(x='eigentime', y= 'Phi3', ax=ax1, label=r'$\Phi_3$', color='#969696')
dfPhi4.plot(x='eigentime', y= 'muG', ax=ax1, label=r'$\mu_G$', color='#636363')


ax1.set_xlabel(r'$\tau$', labelpad=0)
ax1.set_ylabel(r'$\log\,\vartheta$', labelpad=2)

plt.legend(bbox_to_anchor=(0.1, 0.02, 0.4, .502), loc=3,
       ncol=2, mode="expand", borderaxespad=0., frameon=False)

fig.set_size_inches(width, height)
fig.savefig('Resp_5A2.pdf')

################################################################################    Reduction 3

dfPhi2=pd.read_csv('Figures/CSV/figure_5c_panel1_param_Phi2.csv', header=None)
dfPhi2.columns = ['eigentime', 'Phi2']

#
dfPhi4=pd.read_csv('Figures/CSV/figure_5c_panel1_param_muG.csv', header=None)
dfPhi4.columns = ['eigentime', 'muG']



fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.14, bottom=.15, right=.99, top=.97)

dfPhi2.plot(x='eigentime', y= 'Phi2', ax=ax1, label=r'$\Phi_2$', color='#636363')
dfPhi4.plot(x='eigentime', y= 'muG', ax=ax1, label=r'$\mu_G$', color='#969696')


ax1.set_xlabel(r'$\tau$', labelpad=0)
ax1.set_ylabel(r'$\log\,\vartheta$', labelpad=2)

plt.legend(bbox_to_anchor=(0.1, 0.02, 0.4, .502), loc=3,
       ncol=2, mode="expand", borderaxespad=0., frameon=False)

fig.set_size_inches(width, height)
fig.savefig('Resp_5A3.pdf')