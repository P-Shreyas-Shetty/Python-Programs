'''
    Solution of pde Uxx + Uyy = A*Utt
    dx = dy = d
    dt = dt
    
    using finite difference method
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
height = 500
width = 500
k=1
A = 2
d = 0.01
dt = 0.01
uk_2 = np.zeros((height, width)) #u(k-2) state
uk_1 = np.zeros((height, width)) #u(k-1) state
uk = np.zeros((height, width)) #u(k) state

def inititial():
    '''Set Initial conditions'''
    global uk, uk_1, uk_2
    for i in range(height):
        for j in range(width):
            uk_1[i][j] = abs(np.cos(100*j*i*d**2))
            uk_2[i][j] = abs(np.cos(100*j*i*d**2+1))

inititial()

def nxtstate():
    global uk_2, uk_1, uk, k
    for i in range(height-1):
        for j in range(width-1):
            uk[i][j] = (dt**2/A)*(4*uk_1[i][j] + uk_1[i-1][j] + uk_1[i+1][j] + 
                        uk_1[i][j+1] + uk_1[i][j-1])/d**2 - (2*uk_1[i][j] + uk_2[i][j])
    uk_2 = uk_1
    uk_1 = uk
    print("Sim time = %0.2fs"%(k*dt))
    k+=1
    return uk

im = ax.imshow(nxtstate(), animated=True)

def update(*args):
    
    im.set_array(nxtstate())
    return im,
ani = anim.FuncAnimation(fig, update, interval=50, blit=True)
plt.show()

