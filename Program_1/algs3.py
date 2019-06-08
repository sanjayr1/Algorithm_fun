
import csv
import ast

def indegree(digraph):
    '''
    input: digraph represented as adjacency list
    return: dict that maps nodes to indegrees

    Count # of times a nodes shows up in the edge list of adj list since that determines
    how many nodes go into it
    '''
    d = {}
    for key,value in digraph.items():
        d[key] = 0

    for i,j in digraph.items():
        for k in j:
            if k in d.keys():
                d[k] += 1

    return d


#Tests
#A = {2:[5], 3:[5], 5:[3, 7], 7:[2]}
# B = {1:[2,3,4], 2:[1,3,4], 3:[1,2,4], 4:[1,2,3]}
# C = {1:[], 2:[4], 3:[1,2], 4:[2]}
#print(indegree(A))
# print(indegree(B))
# print(indegree(C))


#load adj list from output of 1
with open('alg_1.csv', 'r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}
    mydict = {int(k):ast.literal_eval(v) for k,v in mydict.items()}


#print(mydict)
#print(indegree(mydict))

output = indegree(mydict)

#save to csv
# with open('alg_3.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in output.items():
#        writer.writerow([key, value])