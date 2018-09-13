# -*- coding: utf-8 -*-
"""
Created on Sat Sep 01 12:04:34 2018

@author: Gianna
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy

plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
plt.rc('text', usetex=False)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)
plt.rc('legend', fontsize=5)
width = 3.0
golden_mean = (np.sqrt(5)-1.0)/2.0   # aethestic ratio
height = width*golden_mean

################################################################################    Reduction 1

df1=pd.read_csv('Figures/CSV/figure_3c_panel1_orig.csv', header=None)
df1.columns = ['tmp', 'eigs']
df1['index'] = df1.index

df1log=pd.read_csv('Figures/CSV/figure_31_panel2_log.csv', header=None)
df1log.columns = ['tmp', 'eigslog']
df1log['indexlog'] = df1log.index


fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.15, bottom=.185, right=.99, top=.985)
df1.plot.scatter(x= 'index', y= 'eigs', marker='*', ax=ax1, s=9, color='k')
df1log.plot.scatter(x= 'indexlog', y= 'eigslog', marker='d', ax=ax1, s=9, color='k')
ax1.set_ylabel('Hessian eigenvalues', labelpad=3)
ax1.set_xlabel('Ellipsoid axis', labelpad=3)
fig.set_size_inches(width, height)
fig.savefig('Resp_spectrum0.pdf')
################################################################################    Reduction 2

df2=pd.read_csv('Figures/CSV/figure_31_panel2.csv', header=None)
df2.columns = ['tmp', 'eigs']
df2['index'] = df2.index

################################################################################    Reduction 3

df3=pd.read_csv('Figures/CSV/figure_32_panel2.csv', header=None)
df3.columns = ['tmp', 'eigs']
df3['index'] = df3.index

################################################################################    Reduction 4

df4=pd.read_csv('Figures/CSV/figure_33_panel2.csv', header=None)
df4.columns = ['tmp', 'eigs']
df4['index'] = df4.index

############################################## Terrible way to plot the spectra
fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.15, bottom=.18, right=.99, top=.985)

offset = 0.15
e1 = df1['eigs'].as_matrix()
e2 = df2['eigs'].as_matrix()
e3 = df3['eigs'].as_matrix()
e4 = df4['eigs'].as_matrix()

[ax1.axhline(y=e1[i], xmin=0.05, xmax=0.05+offset,  linewidth=1, color='k') for i in scipy.arange(len(e1))]
[ax1.axhline(y=e2[i], xmin=0.3, xmax=0.3+offset, linewidth=1, color='k') for i in scipy.arange(len(e2))]
[ax1.axhline(y=e3[i], xmin=0.55, xmax=0.55+offset, linewidth=1, color='k') for i in scipy.arange(len(e3))]
[ax1.axhline(y=e4[i], xmin=0.8, xmax=0.8+offset, linewidth=1, color='k') for i in scipy.arange(len(e4))]

ax1.set_ylabel('Hessian eigenvalues', labelpad=3)
ax1.set_xlabel('MBAM iteration', labelpad=3.5)
# Add labels
ax1.set_xticks([0.05+offset/2, 0.3+offset/2, 0.55+offset/2, 0.8+offset/2 ])
xlabels = ['%s' % n for n in  scipy.arange(4)]
ax1.set_xticklabels(xlabels, verticalalignment='bottom',
                 rotation=0, horizontalalignment='center')
for l in ax1.get_xticklabels():
    l.set_y(l.get_position()[1] - 0.065)
#for l in ax1.get_xticklines():
#    l.set_visible(False)
    
#ax1.set_yticks([-20,-15,-10,-5,0]) 
    
fig.set_size_inches(width, height)
fig.savefig('Resp_spectra.pdf')