
from algs2 import clique
from random import choices as ch
from algs6 import plot
import matplotlib.pylab as plt
import csv
import ast

def matthewGraph(d,n):

    #start with clique
    c = clique(d)

    #list of n-d nodes that need to be attached
    leftover = [x for x in range(d+1, n+1)]

    #get next node in n-d list and add it to dict
    for node in leftover:

        #current indegree probabilities
        current_indegree_prob = {}
        for key,value in c.items():
            current_indegree_prob[key] = 1
        for i,j in c.items():
            for g in j:
                if g in current_indegree_prob.keys():
                    current_indegree_prob[g] += 1
        total = sum(current_indegree_prob.values())
        for key in current_indegree_prob:
            current_indegree_prob[key] /= total

        #take random sample of d nodes with replacement from current nodes in graph, with weights based
        # on their current indegree distribution:

        sample_nodes = set(ch(population=list(current_indegree_prob.keys()), weights=list(current_indegree_prob.values()), k=d))

        #append set of nodes to list of new node
        c[node] = list(sample_nodes)

    return c


#Tests
#print(matthewGraph(3,7))
#print(matthewGraph(10,1000))

output = matthewGraph(3,20)

plot(output)

#save to csv
# with open('alg_9.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in output.items():
#        writer.writerow([key, value])