import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np


def solve_linear_system(n, a, x0, dt=0.01):
    '''
    Returns a GENERATOR that when called next, returns values in next tick i.e at time t+dt
    Solves system of the form: xi'(t) = a[i]0.x0(t) + a[i]1.x1(t) + ... + a[i]n.xn(t) ;  where 0 < i < n-1
    n: Integer; number of equations in the system
    a: nxn matrix of coefficients a[i][k]; i,n in range(0, n-1)
    x0: List of xi(0), i.e. initial condition

    Equation is solved using regular N-R method:
        x'(t) = (x(t+dt)-x(t))/dt =>x(t+dt) = x'(t)dt + x(t)
    '''
    a = np.array(a, ndmin=2) #make sure a is np array
    xt = np.array(x0, ndmin=2).T
    while True:
        xt = dt*(a@xt) + xt
        yield xt.T


def animate_system_of_lin_de(n, a, x0, dt=0.01, tmax=10, ylim=(-20, 20)):
    #define generator first
    x0 = np.array(x0, ndmin=2)
    dgen = solve_linear_system(n, a, x0, dt)
    fig = plt.figure()
    ax = plt.axes(xlim=(0,tmax), ylim=ylim)
    running_x = [[x0[0][k]] for k in range(n)]
    running_t = [0]
    #print(running_x, running_t)
    #exit()
    lines = [ax.plot(running_t, running_x[k], label="x%d(t)"%k)[0] for k in range(n)]

    def init():
        return lines

    def animate(i):

        if(running_t[-1]<=tmax): 
            xt = next(dgen) #generate data for next tick
            running_t.append(running_t[-1]+dt)
            for k in range(n):
                running_x[k].append(xt[0][k])
                lines[k].set_data(running_t, running_x[k])
        return lines
    plt.style.use('seaborn-pastel')
    anim = FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=10, blit=True)

    plt.legend()
    plt.show()
    
animate_system_of_lin_de(
    3,
    [[0.1, -0.5, 0.1],
     [1,  -0.2, 0.1],
     [0.3, 1, -0.4]],
    [1,-1, 0],
    dt=0.01,
    tmax=40,
    ylim=(-2, 5)
)