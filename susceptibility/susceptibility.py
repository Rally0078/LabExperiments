import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Helvetica",
    "font.size" : 14
})

df = pd.read_csv("data.csv")
fieldsq = df['fieldsq'].to_numpy()
soln1 = df['soln1'].to_numpy()
soln2 = df['soln2'].to_numpy()

reg1 = linregress(fieldsq * 1000000, soln1)
reg2 = linregress(fieldsq * 1000000, soln2)

d1 = 1.0417
d2 = 1.1202
g = 980
chiw = -0.72e-6

m11 = 37.4
m12 = 102.3
m13 = 99.7

m1w = m13 - m11
m1s = m12 - m13

m21 = 146.2
m22 = 269.2
m23 = 256.0

m2w = m23 - m21
m2s = m22 - m23
print(f"Solution 1: mass of water = {m1w:.3f}, mass of dissolved salt = {m1s:.3f}, density = {d1:.3f}")
print(f"slope for solution 1 = {reg1.slope}")
print(f"Solution 2: mass of water = {m2w:.3f}, mass of dissolved salt = {m2s:.3f}, density = {d2:.3f}")
print(f"slope for solution 1 = {reg2.slope}")

chi1 = 2 * d1 * g * reg1.slope 
chi2 = 2 * d2 * g * reg2.slope 
chiM1 = chi1/d1
chiM2 = chi2/d2
print(f"Mass susceptibility of solution 1 = {chiM1}")
print(f"Mass susceptibility of solution 2 = {chiM2}")

chiS1 = (chiM1 - m1w/(m1s + m1w) * chiw) * (m1s + m1w)/m1s
chiS2 = (chiM2 - m2w/(m2s + m2w) * chiw) * (m2s + m2w)/m2s

print(f"Mass susceptibility of salt 1 = {chiS1}")
print(f"Mass susceptibility of salt 2 = {chiS2}")

print(f"Molar susceptibility of solution 1 = {chiS1 * 169}")
print(f"Molar susceptibility of solution 2 = {chiS2 * 169}")


fig, ax = plt.subplots(figsize=(13,9))
ax.plot(fieldsq, soln1, 'o-')
ax.set_xticks(np.arange(0, 120, 10))
ax.set_xlim(0, 100)
ax.set_yticks(np.arange(0, 0.055, 0.005))
ax.set_ylim(0, 0.050)
ax.margins(x = 0.005, y=0)
ax.grid()
ax.set_title(r'$h$ vs $H^2$ for Solution 1')
ax.set_xlabel(r'Magnetic field squared ($kG^2$)')
ax.set_ylabel(r'Rise of solution ($cm$)')
fig.tight_layout()
plt.savefig("soln1.jpg", bbox_inches='tight', dpi=120)
plt.close()

fig, ax = plt.subplots(figsize=(13,9))
ax.plot(fieldsq, soln2, 'o-')
ax.set_xticks(np.arange(0, 120, 10))
ax.set_xlim(0, 100)
ax.set_yticks(np.arange(0, 0.11, 0.01))
ax.set_ylim(0, 0.10)
ax.margins(x = 0.005, y=0)
ax.grid()
ax.set_title(r'$h$ vs $H^2$ for Solution 2')
ax.set_xlabel(r'Magnetic field squared ($kG^2$)')
ax.set_ylabel(r'Rise of solution ($cm$)')
fig.tight_layout()
plt.savefig("soln2.jpg", bbox_inches='tight', dpi=120)
plt.close()