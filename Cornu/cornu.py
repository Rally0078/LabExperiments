#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# <h3>Importing data from csv</h3>

# In[16]:


df = pd.read_csv('cornu1.csv')


# <h3>Order numbers sorted for plotting</h3>

# In[17]:


order = df['order'].to_numpy()
order.sort()


# <h3>Plot four graphs and obtain the slopes for each plot using linear regression</h3>

# In[18]:


dsqlong = df['dsqlong'].to_numpy()
dsqlong.sort()
a, b = np.polyfit(order, dsqlong, deg = 1)
print('slope = ', a)
print('reciprocal slope = ', 1/a)
plt.scatter(order, dsqlong)
plt.plot(order, a*order+b)
plt.xlabel("Order of interference fringe")
plt.xticks(order)
plt.ylabel("Diameter squared (mm^2)")
plt.title("Longitudinal diameter for m1 = 100g")
plt.savefig('dsqlong.jpeg', dpi= 200)
plt.show()


# In[19]:


dsqtransv = df['dsqtransv'].to_numpy()
dsqtransv.sort()
a, b = np.polyfit(order, dsqtransv, deg = 1)
print('slope = ', a)
print('reciprocal slope = ', 1/a)
plt.scatter(order, dsqtransv)
plt.plot(order, a*order+b)
plt.xlabel("Order of interference fringe")
plt.xticks(order)
plt.ylabel("Diameter squared (mm^2)")
plt.title("Transverse diameter for m1 = 100g")
plt.savefig('dsqtransv.jpeg', dpi = 200)
plt.show()


# In[20]:


dsq150long = df['dsq150long'].to_numpy()
dsq150long.sort()
a, b = np.polyfit(order, dsq150long, deg = 1)
print('slope = ', a)
print('reciprocal slope = ', 1/a)
plt.scatter(order, dsq150long)
plt.plot(order, a*order+b)
plt.xlabel("Order of interference fringe")
plt.xticks(order)
plt.ylabel("Diameter squared (mm^2)")
plt.title("Longitudinal diameter for m2 = 150g")
plt.savefig('dsq150long.jpeg', dpi = 200)
plt.show()


# In[21]:


dsq150transv = df['dsq150transv'].to_numpy()
dsq150transv.sort()
a, b = np.polyfit(order, dsq150transv, deg = 1)
print('slope = ', a)
print('reciprocal slope = ', 1/a)
plt.scatter(order, dsq150transv)
plt.plot(order, a*order+b)
plt.xlabel("Order of interference fringe")
plt.xticks(order)
plt.ylabel("Diameter squared (mm^2)")
plt.title("Transverse diameter for m2 = 150g")
plt.savefig('dsq150transv.jpeg', dpi = 200)
plt.show()

