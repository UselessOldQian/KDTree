import random
from KDTree import createKDTree,findNN
from brute_force import iterator
from util import plot,plot_circle
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    # number of locations
    # list_len = 10000
    # number of nearest location want to find
    k = 30

    # data_list = []
    # for i in range(list_len):
    #     data_list.append((random.randint(0,10000),random.randint(0,10000)))
    # root = createKDTree(data_list)

    query = (42.286654,-71.130749)
    providers = pd.read_csv("MA_vac_provider.csv")
    data_list = []
    for i in range(len(providers)):
        data_list.append([providers.iloc[i]['latitude'],
                          providers.iloc[i]['longitude'],
                          providers.iloc[i]['provider_location_guid'],
                          providers.iloc[i]['loc_name']])

    root = createKDTree(data_list)
    [res,max_dist,full_info] = findNN(root,query, k=k)
    res2 = iterator(query, data_list, k)

    plot(data_list,color='#88c999')
    plot([query],size=10)
    plot(res,color="blue")

    plot_circle(query[0],query[1],max_dist)
    plt.show()
    for node in full_info:
        print(node.address)
