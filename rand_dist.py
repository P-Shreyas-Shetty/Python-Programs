'''
Create random distribution centered around a N-D curve.
Still incomplete. Works properly with only parameters<=2
when functions are given in parametric form.
'''

import numpy as np
from numbers import Number
from pprint import pprint
from itertools import product



def rand_dist(function, samples, dims_num=2, sigma=0.01, coordinate_range=None, seed=42, sampling=100):
    if isinstance(function, (list, tuple)) and len(function) != dims_num:
        raise ValueError("In parametric form length of function list should be same as dimension of coordinates")
    if callable(function):
        if coordinate_range == None:
            points = [np.linspace(0, 1, sampling) for _ in range(dims_num-1)]
        elif isinstance(coordinate_range, Number):
            points = [np.linspace(0, coordinate_range, sampling) for _ in range(dims_num-1)]
        elif hasattr(coordinate_range, '__getitem__') and hasattr(coordinate_range[0], '__getitem__'):
            points = [np.linspace(coordinate_range[i][0], coordinate_range[i][1], sampling)
                for i in range(dims_num-1)]
        else:
            points = [np.linspace(0, coordinate_range[i], sampling) for i in range(dims_num-1)]
        points1 = product(*points)
        points = np.array([[*X,function(*X)] for X in points1]).T

    else:
        if coordinate_range==None:
            points = [np.array([function[i](np.linspace(0, 1, sampling)) for i in range(dims_num)])]
        elif isinstance(coordinate_range, Number):
            points = [np.array([function[i](np.linspace(0, coordinate_range, sampling))]).flatten() for i in range(dims_num)]
        else:
            points = [
                function[i](np.linspace(coordinate_range[0], coordinate_range[1], sampling)) for i in range(dims_num)
                ]
                

    rand_points = []
    for row in points:
        np.random.seed(seed)
        rand_points.append(
            np.array([np.random.normal(np.random.choice(row), scale=sigma) for _ in range(samples)])
        )
    return rand_points
if __name__=='__main__':
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from time import time
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    t0 = time()
    x,y,z, z0 = rand_dist(lambda x,y,z:(1-(x**2+y**2+z**2))**.5, 10000, 4, coordinate_range=[[-1,1],[-1,1],[-1,1]], sigma=0.05 , seed=134)
    t1 = time()
    print("Computation time = %.3fs"%(t1-t0))
    ax.scatter(z,y,z)
    plt.show()
    

    
