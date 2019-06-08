# Algorithms for data science

# TLDR: Check out Program 4 for the most fun

# Program 1
- Implement efficeint algorithms to compute and plot the indegree distributuion of the nodes in a digraph -- explore scientific papers and associated citations to see if cited papers are chosen according to a probabilistic model (popularity begets more popularity) or whether the choices reflect a deep understanding of the papers cited. 
  - Represent a set of scientific papers as nodes in a digraph, and edges from paper `i` to paper `j` if `i` cites `j`
--- Each task written in corresponding algs*.py file
1) Create `loadGraph(nodeFile, edgeFile)` function that reads in our nodes and edges and returns an adjacency list representation of corresponding digraph
2) Create `clique()` function that returns digraph `K_n`
3) Calculate `indegree(digraph)` that returns a dictionary that maps nodes to indegrees
4) Calculate `avgOutDegree(digraph)` that returns the average outdegree of all nodes in the graph
5) Calcuate `indegreeDistribution(digraph)`
6) Log-log plot of the indegree probability distribution of the digraph in `citationgraph.jpg`
7) `randomDigraph(n,p)` generates a directed graph `G(V,E)` of n nodes, where for each pair `u,v`, the probability that the edge is in `E` is `p`
8) Generate a random digraph with the same number of nodes as the citation graph, choose a value of `p` such that the expected number of edges in this graph is equal to the number of edges in the dataset. Plot of the indegree probability distribution is in `randomgraph.jpg`
9) Write code for a Matthew Graph (used to model popularity as a network phenomenon) using `matthewGraph(d,n)`
10) Generate a Matthew Graph with the same number of nodes as the dataset and set d to the average outdegree in the dataset. Plot of the indegree probability is in `matthewgraph.jpg`


# Program 2
- Small World Phenomenon: Experimentally verify if this property holds on a subset of Facebook data
- Given datasets of nodes and edges representing an undirected graph:
  - Implement a queue class
  - Create a `loadGraph()` function to represent the nodes and edges as an adjacency list
  - Implement the Breadth-First-Search algorithm that returns a dictionary that maps each node in the graph to the distance from the starting node `s`
  - Compute the distribution of distances in the graph, mapping distance to frequency of occurence
  - Compute diameter, mode, and median of distances of the graph
  - Estimate how long it would take to compute the diametere of a Facebook graqph consisting of 2 million nodes and 44 million edges on the same computer

# Program 3
- Divide and Conquer algorithm to locate the supermode element of a list
- Decrease and Conquer algorithm to locate the supermode element of a list
- Recommedation system: measure degree to which the rankings of a common set of movies by two people are similar or different
  - Ranking - list of movie ids, ordered from best to worst
  - System finds someone with similar rankings using a distance function, `d(r,s)`, where `r` and `s` are rankings of the same set of `n` movies from 2 individuals. 
  - Count number of inconsistencies in `s` with respect to `r` -> pair of ids `a` and `b` such that `a` appears before `b` in `r` but after `b` in `s`
 - Nearest neighbor graph of individuals and their movie rankings
 - Reverse nearest neighbor graph of indiividuals and their movie rankings

# Program 4
- Given two Wikipedia pages, a link chain is a list of Wikipedia links that one can follow to get from a start page to a target page, such that each page in the chain is arrived at by following a link in the previous page. 
  - Use Priority Queues to find short link chains from a start page `S` to a target page `T`
  - Compute `priority` of a wiki page based on by exploring the number of shared links between a given page `P` and the target page `T` 
  - Build a priority queue of partial link chains with max heaps, repeatedly remove the highest priority partial chian, get set of links in its current page, compare to target page. If all links in current page and target page match, then you've found the target.
