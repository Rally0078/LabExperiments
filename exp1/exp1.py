#!/usr/bin/env python
# coding: utf-8

# <h1>Transistor as amplifier</h1>

# <h2>Data in table</h2>

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate


# In[2]:


Vin = 0.04
df = pd.read_csv('data.csv')

logf = np.log10(df['Frequency(Hz)'])
gain = 20 * np.log10(df['Output voltage(V)']/Vin)

df.insert(1, 'log f', logf)
df.insert(3, 'Voltage gain(dB)', gain)


# In[3]:


df.head()


# <h2>Mid frequency gain and -3dB calculation</h2>

# In[4]:


mid_gain = float(df['Voltage gain(dB)'].mode())
print(f"Mid frequency gain = {mid_gain:.3f}")
print(f"-3dB (half power) gain = {(mid_gain - 3):.3f}")


# <h2>Plotting the bode plot</h2>
# <h3>Cutoff frequencies:</h3>
# <p>The cutoff frequencies are found by interpolation</p>

# In[5]:


cutoff_freq = interpolate.InterpolatedUnivariateSpline(df['log f'], df['Voltage gain(dB)'] -(mid_gain - 3))
print(f"Cutoff logarithmic frequencies are : {cutoff_freq.roots()}")
freq1 = 10**cutoff_freq.roots()[0]
freq2 = 10**cutoff_freq.roots()[1]
print(f"Cutoff frequencies are: {freq1:.3f} Hz, and {freq2:.3f} Hz")


# <h3>Plot</h3>

# In[6]:


fig = plt.figure(facecolor=(1,1,1))
fig.set_figwidth(16)
fig.set_figheight(9)
x_scale = np.arange(2, 6.25, 0.25)
y_scale = np.arange(12, 45, 2)

plt.xticks(x_scale)
plt.yticks(y_scale)

plt.plot(df['log f'], df['Voltage gain(dB)'], label = 'Voltage gain')
plt.hlines(mid_gain-3, 3, 6, colors='orange', label='-3dB gain',linestyles='dashed')
plt.vlines(cutoff_freq.roots(), 10, (mid_gain - 3), colors='black', label='cutoff frequency',linestyles='dashed')

plt.xlabel('log f')
plt.ylabel('Voltage gain(dB)')
plt.legend()
plt.show()

