# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:11:57 2018

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

# Load data
df=pd.read_csv('Figures/CSV/figure_2a_panel1_temp1.0um.csv', header=None)
df.columns = ['Time', 'Rate', 'Error', 'Error1']
df.plot(x='Time', y= 'Rate', yerr='Error', ax=ax1, fmt='ko',linewidth=0.5, ecolor='k', capsize=1, grid='on', ms=1, legend=False)
# Load fit
df=pd.read_csv('Figures/CSV/figure_2a_panel2_temp1.0um.csv', header=None)
df.columns = ['Time', 'Rate']
df.plot(x='Time', y= 'Rate', ax=ax1, color='g', lw=1, grid='on', legend=False)

ax1.set_xlabel('Time [h]')
ax1.set_ylabel(r'$CO_2$ flux rate [$mg\,C /(gh)$]')

fig.set_size_inches(width, height)
fig.savefig('2A.pdf')

plt.show()