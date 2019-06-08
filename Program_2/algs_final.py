##Sanjay Roberts HW 2 Algorithms

import numpy as np
import time

start = time.time()


class Queue:
    def __init__(self, dt, size):
        self.dt = str(dt)
        self.queue = size * [None]
        self.current_size = 0
        self.max_size = size
        self.head = 0
        self.tail = self.max_size - 1
        self.head_element = None
        self.tail_element = None

    def enqueue(self, element):

        if self.dt != str(type(element)):
            return "Not correct datatype"

        if self.full():
            return "Queue full. Can't add element"

        self.tail = (self.tail + 1) % self.max_size
        self.queue[self.tail] = element
        self.current_size += 1

        self.head_element = self.queue[self.head]
        self.tail_element = self.queue[self.tail]

        return None

    def dequeue(self):
        if self.empty():
            return "Queue empty. Can't remove element"

        popped = self.head_element
        self.head = (self.head + 1) % self.max_size
        self.current_size -= 1

        self.head_element = self.queue[self.head]
        self.tail_element = self.queue[self.tail]

        return popped

    def empty(self):
        return self.current_size == 0

    def full(self):
        return self.current_size == self.max_size


def loadGraph(nodeFile, edgeFile):
    '''
    input: file with nodes and file with edges
    return: undirected graph represented as an adjacency list
    '''
    d = {}

    # load file of nodes, convert to a set of ints
    nodes = open(nodeFile, "r")
    nodes = nodes.read().split()
    nodes = [int(i) for i in nodes]
    for i in nodes:
        d[i] = []

    # load file of edges, convert to a set of tuples of ints
    edges = open(edgeFile, "r")
    edges = edges.readlines()
    edges = [i.strip('\n') for i in edges]
    edges = [i.replace(" ", ",") for i in edges]
    edges = [i.split(',') for i in edges]
    edges = [[int(j) for j in i] for i in edges]
    for j in edges:
        d[j[0]].append(j[1])
        d[j[1]].append(j[0])
    return d


def BFS(G,s):
    q = Queue(int, len(G))
    n = len(G.keys())
    d = {}
    for k in G.keys():
        d[k] = n
    d[s] = 0
    q.enqueue(s)
    while not q.empty():
        u = q.dequeue()
        for i in G[u]:
            if d[i] == n:
                d[i] = d[u] + 1
                q.enqueue(i)
    return d


def distanceDistribution(G):
    d = {}
    for k in G.keys():
        d[k] = BFS(G, k)
    list_dist = []
    for s, r in d.items():
        list_dist.append(list(r.values()))
    flat_list = [item for sublist in list_dist for item in sublist]
    flat_list = list(filter(lambda a: a != 0, flat_list))
    distribution_dict = {}
    for item in flat_list:
        if item in distribution_dict:
            distribution_dict[item] += 1
        else:
            distribution_dict[item] = 1
    return distribution_dict


def diameter(G):
    d = distanceDistribution(G)
    return max(d)


def mode(G):
    d = distanceDistribution(G)
    return max(d, key=d.get)


def median(G):
    d = distanceDistribution(G)

    med_list = []
    med_list = np.array(med_list)

    for k,v in d.items():
        temp_list = np.full((1, v), k)
        med_list = np.concatenate((med_list, temp_list), axis=None)
    return np.median(med_list)


output = loadGraph("nodes.txt", "edges.txt")

print(distanceDistribution(output))
print(mode(output))
print(median(output))
print(diameter(output))

end = time.time()

print(end-start)










