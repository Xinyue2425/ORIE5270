from pyspark import SparkConf, SparkContext
import numpy as np


def add_col_mat(line):
    """
    add column index to the matrix elements
    :param line: each line
    :return: [column, [row, element]]
    """
    for i in line[1]:
        yield [i[1], [line[0],i[0]]] # [column, [row, element]]
def add_row_v(line):
    """
    add row index to the vector elements
    :param line: each line
    :return: [row,element]
    """
    for i in range(len(line)):  # [row_v,element_v]
        yield [i,line[i]]
def matrix_n_p_vec_p_1(matrix_txt,vector_txt):
    """
    calculate the dot product of a matrix(n*p) and a vector(p*1) where n is very large while p is small
    :return: the result(vector)
    """
    # create Spark context with Spark configuration
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    # read input text file to RDD
    vector = sc.textFile("vector_p_1.txt")
    matrix = sc.textFile("matrix_n_p.txt")
    vector = vector.map(lambda l: [float(i) for i in l.split(",")]).collect() 
    matrix = matrix.map(lambda l: [float(i) for i in l.split(",")]).cache()
    result = matrix.flatMap(lambda l: [np.dot(l,vector[0])]).collect()
    sc.stop()
    return result
    
def matrix_n_n_vec_n_1(matrix_txt,vector_txt):
    """
    calculate the dot product of a matrix(n*n) and a vector(n*1) where n is very large
    :return: the result(vector)
    """
    # create Spark context with Spark configuration
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    # read input text file to RDD
    vector = sc.textFile(vector_txt)
    matrix = sc.textFile(matrix_txt)
    
    vector = vector.map(lambda l: [float(i) for i in l.split(",")]).cache() 
    vector = vector.flatMap(add_row_v)
    
    matrix = matrix.map(lambda l: [float(i) for i in l.split(",")]).cache()
    matrix = matrix.map(lambda l: [int(l[0]), [[l[i+1],i]for i in range(len(l)-1)]])   
    # [row, [column, element]]
    
    matrix = matrix.flatMap(add_col_mat)  # [column, [row, element]]  
    matrix_join = matrix.join(vector)
    matrix_temp = matrix_join.map(lambda l: (l[1][0][0], l[1][0][1]*l[1][1]))
    matrix_temp.collect()
    fin_result = matrix_temp.reduceByKey(lambda n1,n2:n1+n2).map(lambda l:l[1]).collect()
    sc.stop()
    return fin_result

if __name__ == '__main__':
    print(matrix_n_p_vec_p_1("/Users/xinyuelyu/Desktop/matrix_n_p.txt","/Users/xinyuelyu/Desktop/vector_p_1.txt"))
    print(matrix_n_n_vec_n_1("matrix_n_n.txt","vector_n_1.txt"))
