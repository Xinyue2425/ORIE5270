import numpy as np
def detect_negative_cycle(name_txt_file):
    """
    detect the negative circle in graph using Bellman Ford algo
    :param name_txt_file: read the graph info from the txt file
    :return: whether there is a negative cycle path or not
    """
    # read the graph_info from the txt file
    f = open(name_txt_file, 'r')
    graph_def = f.read()
    graph_def= graph_def.split("\n")
    i=1
    while(i<len(graph_def)):
        if graph_def[i] !="":
            graph_def[i] = eval(graph_def[i])
            if type(graph_def[i][0]) is not tuple:
                graph_def[i]=list(graph_def[i])
                graph_def[i][0]=str(graph_def[i][0])
                graph_def[i]=[tuple(graph_def[i])]
            else:
                temp_list=[]
                for item in graph_def[i]:
                    item = list(item)
                    item[0]=str(item[0])
                    item = tuple(item)
                    temp_list.append(item)
                graph_def[i]=temp_list    
        else:
            graph_def[i]=[]
        i=i+2
    graph_dict={}
    i=0
    while (i<len(graph_def)):  # 0,2,4,6,8,10,12,14
        graph_dict.update({graph_def[i] : graph_def[i+1]})
        i=i+2
    destination = '8'
    # implement the Bellman Ford algo
    n_node = len(graph_dict.keys()) # the number of nodes in graph
    prev_node = {}  # the previous node dictionary
    distance = {}   # the distance dictionary
    for i in graph_dict.keys():
        distance.update({i : np.inf}) 
        prev_node.update({i : None}) 
        
    distance[destination]= 0
    
    for i in range(n_node-1):
        for key in graph_dict.keys():
            for neighbor in graph_dict[key]:
                u = key
                v = neighbor[0]
                w = neighbor[1]
                if distance[u] != np.inf:
                    new_dist = min (distance[u] + w, distance[v])
                    if new_dist < distance[v]: # there is an update
                        distance[v] = new_dist
                        prev_node[v] = u  # store the path  
    for key in graph_dict.keys():
        for neighbor in graph_dict[key]:
            u = key
            v = neighbor[0]
            w = neighbor[1]
            if distance[u] != np.inf:
                if distance[u] + w < distance[v]:
                    return("There is a negative cycle!")
    return ("There is no negative cycle!")
if __name__ == "__main__":
    print(detect_negative_cycle("graph_negative_cycle.txt"))