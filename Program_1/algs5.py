import csv
import ast
from algs3 import indegree

def indegreeDistribution(digraph):
    '''
    input: digraph represented as adjacency list
    return: computes indegree distribution of nodes in a digraph and returns dict that maps indegree values to
    frequency of occurence

    Get list of indegrees from #3
    get total number of degrees (edges)
    create dict and pu unique in-degree values as keys=0, increment for each encounter
    divide dict values by total # of degrees to get indegree distributions (and sums to 1)
     '''
    d = indegree(digraph)
    indegree_set = set(d.values())
    new_dict = {}

    for t in indegree_set:
        new_dict[t] = 0

    for k,v in d.items():
        if v in new_dict.keys():
            new_dict[v] += 1

    total = sum(new_dict.values())

    for key in new_dict:
        new_dict[key] /= total

    return new_dict


#Tests
# A = {2:[5], 3:[5], 5:[3, 7], 7:[2]}
# B = {1:[2,3,4], 2:[1,3,4], 3:[1,2,4], 4:[1,2,3]}
# C = {1:[], 2:[4], 3:[1,2], 4:[2]}
# print(indegreeDistribution(A))
# print(indegreeDistribution(B))
# print(indegreeDistribution(C))



#load adj list from output of 1
with open('alg_1.csv', 'r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}
    mydict = {int(k):ast.literal_eval(v) for k,v in mydict.items()}


#print(mydict)
#print(indegreeDistribution(mydict))


output = indegreeDistribution(mydict)

#save to csv
# with open('alg_5.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in output.items():
#        writer.writerow([key, value])