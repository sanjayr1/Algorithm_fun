import math
import urllib.request
import time


def WikiChain(start, target):
    current_chain = [start]
    p = PriorityQ(Chain)
    p.Insert(Chain(-1, current_chain))
    already_visited = [start]
    target_wiki = WikiLinks(target)

    while not p.Empty():
        start_wiki = WikiLinks(start)
        if target in start_wiki:
            return current_chain + [target]
        for each in start_wiki:
            if each not in already_visited:
                each_links = WikiLinks(each)
                if target in each_links:
                    return current_chain + [each] + [target]
                each_intersect = (each_links & target_wiki)
                already_visited.append(each)
                p.Insert(Chain(len(each_intersect), current_chain + [each]))
        start = p.ExtractMax().data
        current_chain = start
        start = start[-1]

    return 'PriorityQ is empty. Could not find a path between the start and target'


class PriorityQ:
    def __init__(self, dt, A=None):
        self.dt = str(dt)
        self.q = [] if A is None else self.BuildMaxHeap(A)

    def BuildMaxHeap(self, H):
        if self.dt != str(type(H[0])):
            return "Not correct datatype"
        for i in range(len(H)//2-1, -1, -1):
            self.MaxHeapify(H, len(H), i)
        return H

    def Max(self):
        if not self.Empty():
            return self.q[0]

    def ExtractMax(self):
        if not self.Empty():
            maximum = self.q[0]
            self.q[0] = self.q[len(self.q) - 1]
            self.q.pop()
            self.MaxHeapify(self.q, len(self.q), 0)
            return maximum

    def Empty(self):
        return len(self.q) == 0

    def Insert(self,key):
        if self.dt != str(type(key)):
            return "Not correct datatype"
        self.q.append(key)
        self.q[len(self.q)-1] = -math.inf
        self.IncreaseKey(len(self.q)-1, key)


    def MaxHeapify(self, H, n, i):
        left = self.Left(i)
        right = self.Right(i)
        if left < n and H[left] > H[i]:
            largest = left
        else:
            largest = i
        if right < n and H[right] > H[largest]:
            largest = right
        if largest != i:
            H[i], H[largest] = H[largest], H[i]
            self.MaxHeapify(H, n, largest)
        return H

    def Left(self, i):
        return 2 * i + 1

    def Right(self, i):
        return 2 * i + 2

    def Parent(self,i):
        return (i-1)//2

    def IncreaseKey(self, i, key):
        if 'Chain' in self.dt:
            if self.q[i] < key.priority:
                self.q[i] = key
        else:
            if self.q[i] < key:
                self.q[i] = key
        while i>0 and self.q[self.Parent(i)]<self.q[i]:
            self.q[i], self.q[self.Parent(i)] = self.q[self.Parent(i)], self.q[i]
            i = self.Parent(i)


    def HeapSort(self):
        self.BuildMaxHeap(self.q)
        n = len(self.q)
        for i in range(n-1, 0, -1):
            self.q[0], self.q[i] = self.q[i], self.q[0]
            n = n-1
            self.MaxHeapify(self.q,n,0)

class Chain:
    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


def WikiLinks(name):
   url = str(urllib.request.urlopen("https://en.wikipedia.org/wiki/"+name).read())
   return set([i for i in [u.split("\"")[0] for u in url.split("href=\"/wiki/")[1:]]
                       if (":" not in i)&("#" not in i)&(i not in ["Main_Page", name, ])])


"""
Q5: To find the shortest link chain, first I would need to determine if there exists a chain from start to target, which my code does.
Once I know there exists a chain, then I would keep track of the length of that chain in a variable ’shortest'. Then I would continue following the partial chains that are left in my priorityQ if they are less than ‘shortest’, and continue adding to my priority queue new partial chains if once again they are less than shortest. Then I would need to go through every chain left in the priorityQ and if it returns with a shorter distance, update ‘shortest’. If I extract a chain that is in the priorityQ but longer than ‘shortest’, then I can disregard it. Then I would go through the rest of the priorityQ until it was empty.  This allows me to ‘brute force’ check every option possible for a chain that is less than the length of the one that my code currently finds. 
"""


start = time.time()
print(WikiChain('Multipartite_graph', 'Lip%C3%B3t_Fej%C3%A9r'))
end = time.time()
print(end-start)

start = time.time()
print(WikiChain('Lion','White_House'))
end = time.time()
print(end-start)

start = time.time()
print(WikiChain('fur', 'Pacific_Ocean'))
end = time.time()
print(end-start)

start = time.time()
print(WikiChain('Cora_Barbara_Hennel', 'Sesame_Street'))
end = time.time()
print(end-start)


# Will depend based on the set order, and which of two equal priorities is extracted first:

# ['Multipartite_graph', 'Gary_Chartrand', 'Paul_Erd%C5%91s', 'Lip%C3%B3t_Fej%C3%A9r']
# 35.562721967697144
# ['Lion', 'The_New_York_Times', 'White_House']
# 44.26941990852356
# ['fur', 'Western_Europe', 'Pacific_Ocean']
# 26.333599090576172
# ['Cora_Barbara_Hennel', 'Evansville,_Indiana', 'Public_Broadcasting_Service', 'Sesame_Street']
# 60.156569957733154
