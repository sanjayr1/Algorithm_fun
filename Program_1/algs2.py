import csv

def clique(n):
    '''
    input: int n
    return: digraph K_n represented using an adjacency matrix
    '''
    d = {}
    for i in range(1, n+1):
        d[i] = []
        for j in range(1, n+1):
            if i != j:
                d[i].append(j)

    return d


#Tests
# print(clique(4))
# print(clique(5))


# output = clique(100)
#
# #Save output to csv
# with open('alg_2.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in output.items():
#        writer.writerow([key, value])