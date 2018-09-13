# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:47:58 2018

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
fig.subplots_adjust(left=.16, bottom=.05, right=.99, top=.95)


df=pd.read_csv('Figures/CSV/figure_2a_panel3.csv', header=None)
df.columns = ['randB0', 'logB0']
df['index'] = df.index
df.plot.scatter(x= 'index', y= 'logB0', marker='*', ax=ax1, s=4, color='k')

print('Coefficient of variation B0 is {}'.format(stats.variation(df['logB0'])))


dftrue=pd.read_csv('Figures/CSV/figure_2a_panel1.csv', header=None)
indexarray = np.arange(0,100)
trueval = dftrue.iloc[0][1]*np.ones(100)
ax1.plot(indexarray, trueval, lw=1, color='g')

ax1.set_xlabel('')
ax1.set_ylabel(r'$\log_{10}\,B_0$')

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.get_xaxis().set_ticks([])
ax1.set_ylim(-2,1)

fig.set_size_inches(width, height)
fig.savefig('2C_B0.pdf')

################################################################################ r0
fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.13, bottom=.05, right=.99, top=.95)


df=pd.read_csv('Figures/CSV/figure_2b_panel3.csv', header=None)
df.columns = ['randB0', 'logr0']
df['index'] = df.index
df.plot.scatter(x= 'index', y= 'logr0', marker='*', ax=ax1, s=4, color='k')

print('Coefficient of variation r0 is {}'.format(stats.variation(df['logr0'])))

dftrue=pd.read_csv('Figures/CSV/figure_2b_panel1.csv', header=None)
indexarray = np.arange(0,100)
trueval = dftrue.iloc[0][1]*np.ones(100)
ax1.plot(indexarray, trueval, lw=1, color='g')

ax1.set_xlabel('')
ax1.set_ylabel(r'$\log_{10}\,r_0$')

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.get_xaxis().set_ticks([])
ax1.set_ylim(-4,1)

fig.set_size_inches(width, height)
fig.savefig('2C_r0.pdf')
################################################################################ muG
fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.16, bottom=.05, right=.99, top=.95)


df=pd.read_csv('Figures/CSV/figure_2c_panel3.csv', header=None)
df.columns = ['randB0', 'logmuG']
df['index'] = df.index
df.plot.scatter(x= 'index', y= 'logmuG', marker='*', ax=ax1, s=4, color='k')

print('Coefficient of variation muG is {}'.format(stats.variation(df['logmuG'])))

dftrue=pd.read_csv('Figures/CSV/figure_2c_panel1.csv', header=None)
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
fig.savefig('2C_muG.pdf')

################################################################################ YG
fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.16, bottom=.05, right=.99, top=.95)


df=pd.read_csv('Figures/CSV/figure_2d_panel3.csv', header=None)
df.columns = ['randB0', 'logYG']
df['index'] = df.index
df.plot.scatter(x= 'index', y= 'logYG', marker='*', ax=ax1, s=4, color='k')

print('Coefficient of variation YG is {}'.format(stats.variation(df['logYG'])))
dftrue=pd.read_csv('Figures/CSV/figure_2d_panel1.csv', header=None)
indexarray = np.arange(0,100)
trueval = dftrue.iloc[0][1]*np.ones(100)
ax1.plot(indexarray, trueval, lw=1, color='g')

ax1.set_xlabel('')
ax1.set_ylabel(r'$\log_{10}\,Y_G$')

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.get_xaxis().set_ticks([])
ax1.set_ylim(-3,0)

fig.set_size_inches(width, height)
fig.savefig('2C_YG.pdf')

################################################################################ mR
fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.13, bottom=.05, right=.99, top=.95)


df=pd.read_csv('Figures/CSV/figure_2e_panel3.csv', header=None)
df.columns = ['randB0', 'logmR']
df['index'] = df.index
df.plot.scatter(x= 'index', y= 'logmR', marker='*', ax=ax1, s=4, color='k')
print('Coefficient of variation mR is {}'.format(stats.variation(df['logmR'])))

dftrue=pd.read_csv('Figures/CSV/figure_2e_panel1.csv', header=None)
indexarray = np.arange(0,100)
trueval = dftrue.iloc[0][1]*np.ones(100)
ax1.plot(indexarray, trueval, lw=1, color='g')

ax1.set_xlabel('')
ax1.set_ylabel(r'$\log_{10}\,m_R$')

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.get_xaxis().set_ticks([])
ax1.set_ylim(-6,0)

fig.set_size_inches(width, height)
fig.savefig('2C_mR.pdf')