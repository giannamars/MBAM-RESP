# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:45:33 2018

@author: Gianna
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv('Figures/CSV/figure_1b_panel1_temp1.0um.csv', header=None)
df.columns = ['Time', 'Rate']

dflog=pd.read_csv('Figures/CSV/figure_1c_panel1_temp1.0um.csv', header=None)
dflog.columns = ['Time', 'logRate']

ax1 = df.plot.scatter(x= 'Time', y= 'Rate')
ax1 = dflog.plot.scatter(x= 'Time', y= 'logRate')

plt.show()