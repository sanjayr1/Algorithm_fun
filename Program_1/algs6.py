import csv
import ast
import matplotlib.pylab as plt
from algs5 import indegreeDistribution
import math



def plot(digraph):
    '''
    input: digraph represented as adjacency list
    return: log log plot of indegree distribution of digraph
    '''

    new_dict = indegreeDistribution(digraph)
    x = [math.log(i+1) for i in new_dict]
    y = [math.log(new_dict[j]) for j in new_dict]
    plt.title('Indegree Distribution', fontsize=20)
    plt.xlabel('log of indegree values')
    plt.ylabel('log of frequency of occurrence')
    plt.scatter(x,y)

    return plt.show()



#Tests
# A = {2:[5], 3:[5], 5:[3, 7], 7:[2]}
# B = {1:[2,3,4], 2:[1,3,4], 3:[1,2,4], 4:[1,2,3]}
# C = {1:[], 2:[4], 3:[1,2], 4:[2]}
# print(plot(A))
# print(plot(B))
# print(plot(C))

with open('alg_1.csv', 'r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}
    mydict = {int(k):ast.literal_eval(v) for k,v in mydict.items()}


print(plot(mydict))

