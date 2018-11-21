'''
Simulates ripples
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
height = 200
width = 200
damp = 1
previous_state = np.zeros((height, width))
nxt_state = np.zeros((height, width))

#initial conditions
previous_state[height//2][width//2] = 0.001

previous_state[height//2+1][width//2] = 0
previous_state[height//2-1][width//2] = 0
previous_state[height//2][width//2+1] = 0
previous_state[height//2][width//2-1] = 0

previous_state[height//2+1][width//2+1] = 0
previous_state[height//2+1][width//2-1] = 0
previous_state[height//2-1][width//2+1] = 0
previous_state[height//2-1][width//2-1] = 0

# previous_state[height//3][width//3] = 255

# previous_state[height//3+1][width//3] = 255
# previous_state[height//3-1][width//3] = 255
# previous_state[height//3][width//3+1] = 255
# previous_state[height//3][width//3-1] = 255

# previous_state[height//3+1][width//3+1] = 255
# previous_state[height//3+1][width//3-1] = 255
# previous_state[height//3-1][width//3+1] = 255
# previous_state[height//3-1][width//3-1] = 255

def nxtstate():
    global previous_state, nxt_state
    for i in range(height-1):
        for j in range(width-1):
            nxt_state[i][j] = (previous_state[i][j-1] + previous_state[i-1][j] +
                               previous_state[i][j+1] + previous_state[i+1][j])/2 - nxt_state[i][j]

    nxt_state *= damp
    nxt_state, previous_state = previous_state, nxt_state
    return previous_state


im = ax.imshow(nxtstate(), animated=True)

def update(*args):
    
    im.set_array(nxtstate())
    return im,
ani = anim.FuncAnimation(fig, update, interval=50, blit=True)
plt.show(1)

