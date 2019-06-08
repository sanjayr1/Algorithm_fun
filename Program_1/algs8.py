from algs6 import plot
from algs7 import randomDigraph

'''
    citation graph has 27770 technical papers (the nodes) and 352768 bibliographical references (the edges)

    n(n-1)p = edges
    27770(27769)p = 352768
    p =.00045746

    input: n = 27770, p = .00045746
    return: Plot of the indegree probability distribution

    Wait for 2nd plot to show. For some reason it shows # 6's plot first
'''

matt = randomDigraph(27770, 0.00045746)

plot(randomDigraph(27770, 0.00045746))









