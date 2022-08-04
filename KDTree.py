import numpy

import copy
from KD_node import KD_node
from util import computeDist,get_time

def createKDTree(data_list):
    """
    data_list: Set of data points (unordered)
    return: The root of kdtree constructed
    """
    LEN = len(data_list)
    if LEN == 0:
        return
        # Dimensions of data points
    dimension = len(data_list[0])-1
    # variance
    max_var = 0
    # compute variance for every dimension, and choose the dimension
    # with the largest variance to split
    split = 0
    for i in range(dimension):
        ll = []
        for t in data_list:
            ll.append(t[i])
        var = computeVariance(ll)
        if var > max_var:
            max_var = var
            split = i

    # The data points are sorted according to the data divided into domains
    data_list.sort(key=lambda x: x[split])

    # Select the point with the subscript len / 2(the midpoint) as the segmentation point
    point = data_list[LEN // 2]
    root = KD_node(point=point,split=split)

    # create KDTree recursively
    root.left = createKDTree(data_list[0:(LEN // 2)])
    root.right = createKDTree(data_list[(LEN // 2 + 1):LEN])
    return root


def computeVariance(arrayList):
    """
    arrayList: Stored data points
    return:Returns the variance of a data point
    """
    for ele in arrayList:
        ele = float(ele)
    LEN = len(arrayList)
    array = numpy.array(arrayList)
    sum1 = array.sum()
    array2 = array * array
    sum2 = array2.sum()
    mean = sum1 / LEN
    # D[X] = E[x^2] - (E[x])^2
    variance = sum2 / LEN - mean ** 2
    return variance

@get_time(roundnumber=100)
def findNN(root, query, k=1):
    """
    root:root of KDTree
    query:Query point
    k: number of nearest point want to find
    return: Return the nearest point NN to query point
    """
    # initialize root
    nodeList = []
    candidates = {}
    temp_root = copy.copy(root)
    ##Binary search establishment path
    nodeList, candidates = kdTreeForwardSearch(temp_root, query, nodeList, candidates, k)

    ##Backtracking search
    while nodeList:
        # Use list to simulate the stack, last in, first out
        back_point = nodeList.pop()
        ss = back_point.split
        # Determine whether it is necessary to search in the subspace of the parent node
        if abs(query[ss] - back_point.point[ss]) <= max(candidates.keys()):
            # decide which side to go
            if query[ss] <= back_point.point[ss]:
                temp_root = back_point.right
                if temp_root:
                    nodeList, candidates = kdTreeForwardSearch(temp_root, query,
                                                               nodeList, candidates, k)
            else:
                temp_root = back_point.left
                if temp_root:
                    nodeList, candidates = kdTreeForwardSearch(temp_root, query,
                                                               nodeList, candidates, k)

    # res = []
    root.initialize()
    # for i in candidates:
    #     res.append(candidates[i].point)
    max_dist = max(candidates.keys())
    nearest = []
    for k in candidates.keys():
        nearest.append(candidates[k].point)
    return nearest, max_dist


def kdTreeForwardSearch(root, query, nodeList, candidates, k=1):
    '''

    :param root: the current kd tree node
    :param query: the query point
    :param nodeList: the nodes we visited in this forward search
    :param candidates: the neareast candidates
    :param k: the max size of candidates
    :return: the nodeList and candidates
    '''
    temp_root = root
    while temp_root:
        if temp_root.isvisited == 1:
            break
        nodeList.append(temp_root)
        # compute the distance from query point to the current kd tree node
        dd = computeDist(query, temp_root.point)
        # if the size of candidates is still not exceed k, we simply add the distance to the dict
        if len(candidates) < k:
            candidates[dd] = temp_root
        # otherwise we need to delete the max distance in the dict
        elif max(candidates.keys()) > dd:
            del (candidates[max(candidates.keys())])
            candidates[dd] = temp_root
        temp_root.isvisited = 1

        # The divide dimension of the current node
        ss = temp_root.split
        # decide which side to go
        if query[ss] <= temp_root.point[ss]:
            temp_root = temp_root.left
        else:
            temp_root = temp_root.right
    return nodeList, candidates