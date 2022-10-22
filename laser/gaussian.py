#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import median
from scipy import interpolate


# In[22]:


df = pd.read_csv('data.csv')
cols = []
cols = df.columns


# In[27]:


it = iter(cols)
for col in it:
    x = df[col].to_numpy()
    y = df[next(it)].to_numpy()
    x = x[~np.isnan(x)]
    y = y[~np.isnan(y)]

    med = median(x)
    max_x = max(x)
    peak = np.amax(y)
    width_level = peak/(np.e)**2

    widths = interpolate.InterpolatedUnivariateSpline(x - med, y - width_level)
    print(col + ' Gaussian profile:')
    print(f"Width is {widths.roots()[1]} mm - {widths.roots()[0]} mm = {widths.roots()[1] - widths.roots()[0]} mm")

    plt.vlines(widths.roots()[0], -2, 20, linestyles='dashed', colors = 'k')
    plt.vlines(widths.roots()[1], -2, 20, linestyles='dashed', colors = 'k')
    plt.hlines(width_level, -2,2, linestyles='dashed', colors='r')
    plt.xlabel('Distance from peak of gaussian(mm)')
    plt.ylabel('Current (mA)')
    plt.title(col)
    plt.xticks(np.linspace(-2,2,5))
    plt.plot(x - med, y)
    plt.savefig(col + '.jpg', dpi=200)
    plt.show()


# In[32]:


x = df['dy40cm'].to_numpy()
y = df['iy40cm'].to_numpy()
x = x[~np.isnan(x)]
y = y[~np.isnan(y)]
med = median(x)
max_x = max(x)
peak = np.amax(y)
width_level = peak/(np.e)**2

widths = interpolate.InterpolatedUnivariateSpline(x-med, y - width_level)
print(col + ' Gaussian profile:')
print(f"Width is {widths.roots()[1]} mm - {widths.roots()[0]-0.07} mm = {widths.roots()[1] - widths.roots()[0]+0.07} mm")

plt.vlines(widths.roots()[0]-0.07, -2, 20, linestyles='dashed', colors = 'k')
plt.vlines(widths.roots()[1], -2, 20, linestyles='dashed', colors = 'k')
plt.hlines(width_level, -2,2, linestyles='dashed', colors='r')
plt.xlabel('Distance from peak of gaussian(mm)')
plt.ylabel('Current (mA)')
plt.title(col)
plt.xticks(np.linspace(-2,2,5))
plt.plot(x - med, y)
plt.savefig(col + '.jpg', dpi=200)
plt.show()

