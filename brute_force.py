import heapq
from util import get_time, computeDist

@get_time(roundnumber=100)
def iterator(x, data_list, k):
    '''
    Solve the problem using brute force
    :param x: The query point
    :param data_list: The location list
    :param k: the number of nearest location need to find
    :return: the nearest k location list
    '''
    dis = []
    candidates = []
    for i in range(len(data_list)-1):
        dis.append(computeDist(x, data_list[i]))
    small_value_inds = list(map(dis.index, heapq.nsmallest(k, dis)))
    for i in small_value_inds:
        candidates.append(data_list[i])
    return candidates