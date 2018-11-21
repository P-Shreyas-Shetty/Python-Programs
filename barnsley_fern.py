'''
Program to draw barnsley fern
'''

import matplotlib.pyplot as plt
import numpy as np
import random
N=100000

x = np.zeros(N)
y = np.zeros(N)

for i in range(N-1):
    r = random.random()
    if r<0.01:
        x[i+1], y[i+1] = (0,
                          0.16*y[i])
    elif r<0.86:
        x[i+1], y[i+1] = (0.85*x[i] + 0.04*y[i],
                        -0.04*x[i] + 0.85*y[i] + 1.6)
    elif r<0.93:
        x[i+1], y[i+1] = (0.20*x[i] - 0.26*y[i],
                        0.23*x[i] + 0.22*y[i] + 1.6)
    else:
        x[i+1], y[i+1] = (-0.15*x[i] + 0.28*y[i],
                        0.26*x[i] + 0.24*y[i] + 0.44)
plt.scatter(x, y, marker='o', color='g', s=1)
plt.show()

