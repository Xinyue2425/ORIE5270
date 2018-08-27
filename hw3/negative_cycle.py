import numpy as np
def Bellman_Ford(graph_dict,source,destination, loop_limit):
    """
    find the shortest path from source to destination
    :param graph_dict: the graphy in dictionary format
    :param source: the starting point
    :param destination: the ending point
    :param loop_limit: the largest number of nodes between the source and the destination
    :return: the negative cycle path or there is no negative cycle
    """
    distance = {}   # the distance dictionary
    for i in graph_dict.keys():
        distance.update({i : np.inf}) 
    distance[destination]= 0
    # assume every node is far from the destination except itself
    
    changed_node = [destination] # start from destination
    Node_path = {} # shortest path for each node to the given destination
    for key in graph_dict.keys(): # the key here indicates each source
        Node_path.update({key : None})
    changed_node_temp = []
    
    for i in range(loop_limit-1): # iterate n-1 times (all the nodes except the destination)   
        for current_key in changed_node:
            previous_node = []
            # find all the previous nodes of the current node
            for item in graph_dict.keys(): # key
                for neighbor in graph_dict[item]:
                    if neighbor[0] == current_key:
                        previous_node.append([item,neighbor[1]])

            for pre in previous_node:
                if pre[1] + distance[current_key] < distance[pre[0]]:
                    distance[pre[0]] = pre[1] + distance[current_key]
                    Node_path[pre[0]] = current_key
                    changed_node_temp.append(pre[0])
        if changed_node_temp != []: 
            changed_node = changed_node_temp
            changed_node_temp = []
        else:
            break  # np update anymore
            

    shortest_path = []
    shortest_path.append(source)
    current_key = source
    while (True):
        if Node_path[current_key] == None:
            return "We cannot reach to destination from the source"
        elif Node_path[current_key] == destination:
            shortest_path.append(destination)
            break
        elif Node_path[current_key] in shortest_path:
            shortest_path = shortest_path[shortest_path.index(Node_path[current_key]):]
            break
        else:
            shortest_path.append(Node_path[current_key])
            current_key = Node_path[current_key]

    return [distance[source], shortest_path]

def detect_negative_cycle(name_txt_file):
    """
    detect the negative circle in graph
    :param name_txt_file: read the graph info from the txt file
    :return: the negative cycle path or there is no negative cycle
    """
    # read from txt file
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
        
    for k in graph_dict.keys():
        graph_dict[k].append(['extra_node', 0])
    graph_dict['extra_node'] = []
    n_node = len(graph_dict.keys())
    for k in graph_dict.keys():
        if Bellman_Ford(graph_dict, k, 'extra_node',n_node)[1] < Bellman_Ford(graph_dict, k, 'extra_node', n_node - 1)[1]:
            negative_cycle = Bellman_Ford(graph_dict, k, 'extra_node', n_node)[1]
            print("There is a negative cycle!")
            return negative_cycle
    return "There is no negative cycle!"
if __name__ == "__main__":
    print(detect_negative_cycle("graph.txt"))
