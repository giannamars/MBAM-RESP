# -*- coding: utf-8 -*-
"""
Created on Sat Sep 01 21:27:04 2018

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
width = 3.0
golden_mean = (np.sqrt(5)-1.0)/2.0   # aethestic ratio
height = width*golden_mean



fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.2, bottom=.225, right=.99, top=.96)

###############################################################################  Load data
df=pd.read_csv('Figures/CSV/figure_2a_panel1_temp1.0um.csv', header=None)
df.columns = ['Time', 'Rate', 'Error', 'Error1']
df.plot(x='Time', y= 'Rate', yerr='Error', ax=ax1, fmt='ko',linewidth=0.5, ecolor='k', capsize=1, grid='on', ms=1, legend=False)

################################################################################# Load Reduction 0
df0=pd.read_csv('Figures/CSV/figure_2a_panel2_temp1.0um.csv', header=None)
df0.columns = ['Time', 'Rate']
df0.plot(x='Time', y= 'Rate', ax=ax1, color='g', lw=1, grid='on', label = '0')


################################################################################# Load Reduction 1
df1=pd.read_csv('Figures/CSV/figure_4b_panel2_red_num1.csv', header=None)
df1.columns = ['Time', 'Rate']
df1.plot(x='Time', y= 'Rate', ax=ax1, color='#377eb8', lw=1, grid='on', label='1')

################################################################################ Load Reduction 1
df2=pd.read_csv('Figures/CSV/figure_4b_panel2_red_num2.csv', header=None)
df2.columns = ['Time', 'Rate']
df2.plot(x='Time', y= 'Rate', ax=ax1, color='#e41a1c', lw=1, grid='on', label='2')

################################################################################ Load Reduction 1
df2=pd.read_csv('Figures/CSV/figure_4b_panel2_red_num3.csv', header=None)
df2.columns = ['Time', 'Rate']
df2.plot(x='Time', y= 'Rate', ax=ax1, color='#984ea3', lw=1, grid='on', label='3')

ax1.set_xlabel('Time [h]')
ax1.set_ylabel(r'$CO_2$ flux rate [$mg\,C /(gh)$]')

fig.set_size_inches(width, height)
fig.savefig('Resp_4A.pdf')

############################################################################## Plot the cost
mb = np.arange(0,4)
cost = np.array([1.53473e-34, 1.5347254244335786e-34, 2.561902648266199e-10, 6.117833185955321e-7])

fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.12, bottom=.19, right=.99, top=.92)
ax1.plot(mb, cost, '*', color='k')
ax1.set_xticks([0, 1,2,3 ])
xlabels = ['%s' % n for n in  np.arange(4)]
ax1.set_xticklabels(xlabels, verticalalignment='bottom',
                 rotation=0, horizontalalignment='center')
for l in ax1.get_xticklabels():
    l.set_y(l.get_position()[1] - 0.065)

ax1.set_ylabel('Cost', labelpad=3)
ax1.set_xlabel('MBAM iteration', labelpad=3)

fig.set_size_inches(width, height)
fig.savefig('Resp_4B.pdf')

plt.show()