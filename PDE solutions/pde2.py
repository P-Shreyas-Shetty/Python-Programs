'''
    Solution of pde a*Uxx + b*Uyy = c*Ut/t
    dx = dy = d
    dt = dt
    
    using finite difference method
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
height = 300
width = 300
a = 0.5
b = 0.5
c = 5
k = 1
d = 0.2
dt = 0.2
uk_1 = np.zeros((height, width)) #u(k-1) state
uk = np.zeros((height, width)) #u(k) state

def inititial():
    '''Set Initial conditions'''
    global uk, uk_1
    for i in range(height):
        for j in range(width):
            if i<height//2+1 and j<width//2+1:
                uk_1[i][j] = 0.01
inititial()

def nxtstate():
    global  uk_1, uk, k
    for i in range(height-1):
        for j in range(width-1):
            uk[i][j] = k*(2*uk_1[i][j]*(a+b+1)/d + (a/d)*(uk_1[i+1][j]+uk_1[i-1][j]) +  (b/d)*(uk_1[i][j+1]+uk_1[i][j-1]))*(dt**2)/c
    uk_1 = uk
    k+=1
    return uk

im = ax.imshow(nxtstate(), animated=True)

def update(*args):
    
    im.set_array(nxtstate())
    return im,
ani = anim.FuncAnimation(fig, update, interval=50, blit=True)
plt.show()

