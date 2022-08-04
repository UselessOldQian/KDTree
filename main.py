import random
from KDTree import createKDTree,findNN
from brute_force import iterator
from util import plot,plot_circle
import matplotlib.pyplot as plt

if __name__ == '__main__':
    list_len = 10000
    data_list = []
    for i in range(list_len):
        data_list.append((random.randint(0,10000),random.randint(0,10000)))
    root = createKDTree(data_list)

    query = (random.randint(0,10000),random.randint(0,10000))
    k = 30
    [res,max_dist] = findNN(root,query, k=k)
    res2 = iterator(query, data_list, k)

    #print(sorted(res2))
    plot(data_list,color='#88c999')
    plot([query],size=10)
    plot(res,color="blue")

    plot_circle(query[0],query[1],max_dist)
    plt.show()
    #print(station[station['SiteId']==res[-1][-1]])
