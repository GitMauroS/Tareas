import math

x = math.cos(math.pi/2)
print(x)

from math import sin, pi, cos

y = sin(pi/2)
print(y)

x = cos(y)
print(x)

from math import *

y = sin(pi/2)
print(y)

x = cos(y)
print(x)

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Make data
np.random.seed(19680801)
n = 100
rng = np.random.default_rng()
xs = rng.uniform(23, 32, n)
ys = rng.uniform(0, 100, n)
zs = rng.uniform(-50, -25, n)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(xs, ys, zs)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
