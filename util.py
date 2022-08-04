import math
from time import time
from functools import wraps
import matplotlib.pyplot as plt
import numpy as np

def computeDist(pt1, pt2):
    """
    Calculate the distance between two data points
    return:the distance between pt1 and pt2
    """
    sum = 0.0
    for i in range(len(pt1)):
        sum = sum + (pt1[i] - pt2[i]) * (pt1[i] - pt2[i])
    return math.sqrt(sum)

def get_time(roundnumber=100):
    '''

    :param roundnumber: number of iterate round
    :return: the execute time
    '''
    def get_time_deco(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            start = time()
            for i in range(roundnumber):
                res = func(*args, **kwargs)
            end = time()
            print('%sRunning Time:%.6f' % (func.__name__, (end - start)))
            return res
        return decorator
    return get_time_deco

def plot(point_array, color = 'red', size = 1):
    x = []
    y = []
    for point in point_array:
        x.append(point[0])
        y.append(point[1])
    plt.scatter(x,y,color=color,s=size)

def plot_circle(x,y,r):
    # x axis
    a = np.arange(x-r,x+r,0.001)
    # y axis
    b = np.sqrt(np.power(r,2)-np.power((a-x),2))
    plt.plot(a,y+b,color='r')
    plt.plot(a,y-b,color='r')

