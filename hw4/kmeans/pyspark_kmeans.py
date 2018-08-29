import numpy as np
from operator import itemgetter
from pyspark import SparkContext
from pyspark import SparkConf, SparkContext
import numpy as np
import sys


def assert_equal(list1,list2): #[array,array]  a list of array
    """
    check whether the contents of the two lists are same
    :param list1: the first list of arrays
    :param list2: the second list of arrays
    :return: True if the elements of two lists are same, o.w. False
    """
    if len(list1)!=len(list2):
        return False
    else:
        list1_cp = list1.copy()
        list2_cp = list2.copy()
        for i in range(len(list1_cp)):  # a list of list
            list1_cp[i]=list(list1_cp[i])
            list2_cp[i]=list(list2_cp[i])
        for i in range(len(list1_cp[1])):
            list1_cp = sorted(list1_cp, key = itemgetter(i))
            list2_cp = sorted(list2_cp, key = itemgetter(i))
        return list1_cp==list2_cp

def pyspark_kmeans(centroids_txt, data_txt):
    """
    implement the kmeans method for unsupervised learning
    :param centroids_txt: the text file containing the centroids info
    :param data_txt: the text file containing the data points
    :return: the final centroids (a list)
    """

    # Load the data
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    #"/Users/xinyuelyu/Desktop/centroids.txt"
    centroids = sc.textFile(centroids_txt).map(lambda line: np.array([float(x) for x in line.split(' ')])).collect()
    data = sc.textFile(data_txt).map(lambda line: [0,[np.array([float(x) for x in line.split(' ')]),[0 for i in range(len(centroids))]]]).cache()
    count=0
    for k in range(90):
        old_centroids = centroids

        # (class_id,[point,[distance1,distance2,...]])
        data = data.map(lambda l: (l[0],[l[1][0],[np.linalg.norm(l[1][0] - centroids[i]) for i in range(len(centroids))]])).cache()

        # add the updated class_id
        data = data.map(lambda l: (min(enumerate(l[1][1]), key=itemgetter(1))[0],[l[1][0],l[1][1]])).cache()

        # (class_id,[point,[distance1,distance2,...]])
        data_temp = data.map(lambda l: (l[0],l[1][0].tolist())).cache() # have a class id for each point

        # group the points of the same class
        data_group = data_temp.groupByKey().mapValues(list).cache()

        # calculate the new centroids
        centroids = data_group.map(lambda l: np.mean(l[1],axis=0)).collect()
        count+=1
        if assert_equal(old_centroids,centroids):
            print("The centroids are unchanged!")
            print (count)
            sc.stop()
            return centroids
    sc.stop()
    return centroids

if __name__ == '__main__':
    print(pyspark_kmeans("centroids.txt", "data.txt"))
