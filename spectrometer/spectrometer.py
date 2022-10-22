#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


df = pd.read_csv('data.csv')
df


# In[16]:


incidence = df['incidence'].to_numpy()
emergence = df['emergencedeg'].to_numpy() + (df['emergencemin'].to_numpy())/60

plt.figure(figsize=(8, 6))
plt.plot(incidence, emergence)

x = np.linspace(35, 55, 7)
plt.plot(x, x)

mindev = 48.24
plt.xlabel('Angle of Incidence i')
plt.ylabel('Angle of Emergence i\'')
plt.xticks(np.arange(35,67.5, 2.5))
plt.yticks(np.arange(35,67.5, 2.5))
plt.hlines(mindev, 35, mindev, linestyles='dashed', color='black')
plt.vlines(mindev, 35, mindev, linestyles='dashed', color='black')
plt.plot(incidence, emergence, 'ko')
plt.plot(mindev, mindev, 'ro')

plt.savefig('iVsidash.png', dpi=200)
plt.show()


# In[14]:


deviation = incidence + emergence - 60.5
plt.figure(figsize=(8, 6))
plt.plot(incidence, deviation)

plt.xlabel('Angle of Incidence i')
plt.ylabel('Angle of Deviation D')
plt.xticks(np.arange(35,67.5, 2.5))
plt.yticks(np.arange(35,67.5, 2.5))

plt.savefig('iVsD.png', dpi=200)
plt.show()


# In[22]:


print(f"Angle of minimum deviation from the graph = {np.min(deviation)}")
print(f"Angle of minimum deviation from the equation = {mindev * 2 - 60.5}")

