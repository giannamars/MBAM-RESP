# -*- coding: utf-8 -*-
"""
Created on Sun Sep 02 19:27:29 2018

@author: Gianna
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
plt.rc('text', usetex=False)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)
plt.rc('legend', fontsize=8)
width = 3.0
golden_mean = (np.sqrt(5)-1.0)/2.0   # aethestic ratio
height = width*golden_mean

################################################################################ B0
fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.18, bottom=.05, right=.99, top=.95)


df=pd.read_csv('Figures/CSV/figure_8a_panel3.csv', header=None)
df.columns = ['randB0', 'logPhi2']
df['index'] = df.index
df.plot.scatter(x= 'index', y= 'logPhi2', marker='*', ax=ax1, s=4, color='k')

print('Coefficient of variation Phi2 is {}'.format(stats.variation(df['logPhi2'])))


dftrue=pd.read_csv('Figures/CSV/figure_8a_panel2.csv', header=None)
indexarray = np.arange(0,100)
trueval = dftrue.iloc[0][1]*np.ones(100)
ax1.plot(indexarray, trueval, lw=1, color='g')

ax1.set_xlabel('')
ax1.set_ylabel(r'$\log_{10}\,\Phi_2$')

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.get_xaxis().set_ticks([])
ax1.set_ylim(-2,0)

fig.set_size_inches(width, height)
fig.savefig('Resp_8_Phi2.pdf')

################################################################################ r0
fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.175, bottom=.05, right=.99, top=.95)


df=pd.read_csv('Figures/CSV/figure_8b_panel3.csv', header=None)
df.columns = ['randB0', 'logmuG']
df['index'] = df.index
df.plot.scatter(x= 'index', y= 'logmuG', marker='*', ax=ax1, s=4, color='k')

print('Coefficient of variation muG is {}'.format(stats.variation(df['logmuG'])))

dftrue=pd.read_csv('Figures/CSV/figure_8b_panel2.csv', header=None)
indexarray = np.arange(0,100)
trueval = dftrue.iloc[0][1]*np.ones(100)
ax1.plot(indexarray, trueval, lw=1, color='g')

ax1.set_xlabel('')
ax1.set_ylabel(r'$\log_{10}\,\mu_G$')

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.get_xaxis().set_ticks([])
ax1.set_ylim(-2,-1)

fig.set_size_inches(width, height)
fig.savefig('Resp_8_muG.pdf')