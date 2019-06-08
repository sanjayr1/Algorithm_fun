# Algorithms for data science

# Program 1
-


# Program 2
-

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
