from random import random as rd


def randomDigraph(n,p):
    '''
    input: n nodes, p probability of two nodes connecting
    return: adj list of graph G(V,E)
    number of edges should be (n(n-1)) * p
    '''
    d = {}
    for i in range(1,n+1):
        d[i] = []

    for i in range(1,n+1):
        for j in range(i+1, n+1):
            if rd() < p:
                d[i].append(j)
            if rd() < p:
                d[j].append(i)
    return d


#permutation
#this checks 1-2, 2-1, 1-3, 3-1, 1-4, 4-1, 1-5, 5-1
#then 2-3, 3-2, 2-4, 4-2, 2-5, 5-2
#then 3-4, 4-3, 3-5, 5-3
#then 4-5, 5-4


#Tests
#print(randomDigraph(5, .5))
#print(randomDigraph(10,.2))


















