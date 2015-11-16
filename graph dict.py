'''
graphs:
ref: https://www.python.org/doc/essays/graphs/

 A -> B
    A -> C
    B -> C
    B -> D
    C -> D
    D -> C
    E -> F
    F -> C
'''

graph = {'A': ['B', 'C'],'B': ['C', 'D'],'C': ['D'],'D': ['C'],'E': ['F'],'F': ['C']}

#dir(graph)
#graph.keys()

nodes=graph.keys()
#print("nodes:",nodes)
##len(nodes) => total # nodes

##graph.values()
counter=0
for iter in graph.values():
    counter += len(iter)

#print("#of nodes:",len(nodes))
#print("#of paths:",counter)


def find_all_paths(graph,start,end,path=[]):
    path.append(start)
    print("parent lookup:",graph[start])
    for node in graph[start]:
        print("looking into node:",node)
        if(node in visited_nodes):
            print("visited:",visited_nodes)
            return
        else:
            visited_nodes.append(node);
            if(node == end):
                path.append(node);
                print("1 match found");
                print(path)
                all_paths.append(path)
            else:
                find_all_paths(graph,node,end,path)
    print("all paths found:",all_paths)    

## find path between 2 specific nodes:
visited_nodes=[]
all_paths=[]
find_all_paths(graph,'A','B');
    
