import numpy as np
def find_shortest_path(name_txt_file, source, destination):  # graph is a dictionary
    """
    read from txt file to get the graph info and find the shortest path using Dijkstra algo
    :param name_txt_file: 
    :param source: 
    :param destination: 
    :return: 
    """
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
    
    
    if source not in graph_dict.keys() or destination not in graph_dict.keys():
        return ("Invalid input!")
    else:
        F=[]
        distance= {}   # create a dictionary to record distance from source to each key
        for i in graph_dict.keys():
            distance.update({i:0})

        if source == destination:
            print ("The destination is the same as the source!")
        else:
            for neighbor in graph_dict[source]:
                if destination == neighbor[0]:
                    return ([source,destination],neighbor[1] )
            else:
                for neighbor in graph_dict[source]: # ('2', 4), ('3', 4)
                    distance[neighbor[0]] = distance[neighbor[0]] + neighbor[1]
                    F.append(neighbor[0])
                S=[source]

                while (F!=[]):
                    min_value = np.inf
                    for i in F: # "2", "3"
                        if  (distance[i] <= min_value):
                            f = i
                    F.remove(f)
                    S.append(f)
                    if f==destination:
                        break
                    for neighbor in graph_dict[f]: # ('5', 4), ('6', -2)
                        if neighbor[0] not in S or neighbor[0] not in F:
                            distance[neighbor[0]] = distance[f] + neighbor[1]  
                            #print(distance)
                            # add the weight to the distance
                            F.append(neighbor[0])
                        else:
                            if (distance[f] + neighbor[1] < distance[neighbor[0]]):
                                distance[neighbor[0]]= distance[f] + neighbor[1];
                if destination not in S:
                    return("We can not reach to destination from source!")
                else:
                    return (S, distance[f])

if __name__ == '__main__':
    find_shortest_path("graph.txt", "1", "1")
    print("\n")
    print(find_shortest_path("graph.txt", "1", "2"))
    print("\n")
    print(find_shortest_path("graph.txt", "1", "7"))
    print("\n")
    print(find_shortest_path("graph.txt", "4", "1"))

