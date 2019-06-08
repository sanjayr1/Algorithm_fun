
import csv
import ast

def avgoutdegree(digraph):
    '''
    input: digraph represented as adjacency list
    return: computes average outdegree of the nodes in a digraph

    Count # of edges in adj list for a given node since that will tell how many edges leave that node
    Sum all nodes and sum edges, then average outdegree is edges/nodes
    '''
    d = {}
    for key, value in digraph.items():
        d[key] = len(value)
    # number of nodes
    f = len(d)
    # number of edges
    g = sum(d.values())
    # avg out degree is edges/nodes
    return 'average out degree is ' + str(g/f)


#Tests
# A = {2:[5], 3:[5], 5:[3, 7], 7:[2]}
# B = {1:[2,3,4], 2:[1,3,4], 3:[1,2,4], 4:[1,2,3]}
# C = {1:[], 2:[4], 3:[1,2], 4:[2]}
# print(avgoutdegree(A))
# print(avgoutdegree(B))
# print(avgoutdegree(C))


#load adj list from 1
with open('alg_1.csv', 'r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}
    mydict = {int(k):ast.literal_eval(v) for k,v in mydict.items()}


#print(mydict)
print(avgoutdegree(mydict))

#For our data set the average out degree is 12.703204897371265