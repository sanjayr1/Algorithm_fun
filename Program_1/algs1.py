import csv

def loadDigraph(nodes, edges):
    '''
    input: file with Paper Ids (nodes) and file with Pairs (edges)
    return: digraph represented as an adjacency list
    '''

    d = {}
    for i in nodes:
        d[i] = []
    for j in edges:
        d[j[0]].append(j[1])

    return d


# Tests:
# file1 = [2, 5, 3, 7]
# file2 = [(5,3), (2,5), (5,7), (7,2), (3,5)]
# print(dig(file1, file2))


#load file of nodes, convert to a list of ints
nodes = open("citation_nodes.txt", "r")
nodes = nodes.read().split()
nodes = [int(i) for i in nodes]

#load file of edges, convert to a list of tuples of ints
edges = open("citation_edges.txt", "r")
edges = edges.readlines()
edges = [i.strip('\n') for i in edges]
edges = [i.replace(" ", ",") for i in edges]
edges = [i.split(',') for i in edges]
edges = [[int(j) for j in i] for i in edges]
edges = [tuple(l) for l in edges]

output = loadDigraph(nodes,edges)

#save to a csv to load for later problems
# with open('alg_1.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in output.items():
#        writer.writerow([key, value])