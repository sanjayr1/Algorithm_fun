import csv
import time

# 2b - algorithm to compute distance

def d(r,s):
    #check if lists are same length
    if len(r) != len(s):
        return "Lists are not the same length"
    # check if lists have the same elements
    if sorted(r) != sorted(s):
        return 'lists do not have the same elements in them'

    n = len(r)
    position = {}
    # dict of truth. Already sorted
    for i in range(n):
        position[s[i]] = i
    # run inconsistencies on this list and count the diffs
    k = []
    for i in r:
        k.append(position[i])

    global count
    count = 0
    return inconsistencies(k)

def inconsistencies(list):
    global count

    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]

        #recursive calls on left and right lists
        inconsistencies(left)
        inconsistencies(right)

        left_inc = 0
        right_inc = 0
        full_inc = 0

        while left_inc < len(left) and right_inc < len(right):
            if left[left_inc] < right[right_inc]:
                list[full_inc] = left[left_inc]
                left_inc += 1
            else:
                list[full_inc] = right[right_inc]
                right_inc += 1
                count = count + len(left) - left_inc
            full_inc += 1

        while left_inc < len(left):
            list[full_inc] = left[left_inc]
            left_inc += 1
            full_inc += 1

        while right_inc < len(right):
            list[full_inc] = right[right_inc]
            right_inc += 1
            full_inc += 1
        return count

############################

# 2d - Nearest Neighbor

#load rankings and put in dict, with id as key and ranking list as value

s1 = time.time()
s = time.time()

rankings = open('rankings.txt', 'r')
rankings = rankings.read().split()
the_dict = []
for i in rankings:
    newlist = [i]
    the_dict.append(newlist)

ranking_list = []
for list1 in range(0,len(the_dict)):
    newlist = []
    kk = the_dict[list1]
    for i in kk:
        for w in i.split(','):
            newlist.append(int(w))
    ranking_list.append(newlist)

final_rankings = {words[0]:words[1:] for words in ranking_list}

e = time.time()
print('load rankings and put in dict, with id as key and ranking list as value: {}'.format(e-s))

##################################
s = time.time()

#Run our distance method on each key round robin style and save the output.
output_dict = {}
for key in final_rankings:
    output_dict[key] = {next_key: d(final_rankings[key], final_rankings[next_key]) for next_key in final_rankings if key != next_key}

e = time.time()
print('distance method for every single node against every other node: {}'.format(e-s))


#print(output_dict)

################################

s = time.time()
#find all the minimum values for each inner dict, for each key in the outer dict.
#This will give us our adj list for Nearest Neighbor
adj_dict = {}
for k,v in output_dict.items():
    min_val = min(v.values())
    adj_dict[k] = [sk for sk, sv in v.items() if sv == min_val]

e = time.time()
print('to get adj list for Nearest Neighbors: {}'.format(e-s))

output = adj_dict



#save to csv
# with open('adj_list_NN.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in output.items():
#        writer.writerow([key, value])


############################

# 2e - Reverse Nearest Neighbor

#find all the times a number shows up as the NN
#This will give us our adj list for Reverse Nearest Neighbor

s = time.time()

rnn_dict = {}
for k,v in adj_dict.items():
    rnn_dict[k] = []

for k,v in adj_dict.items():
    for k2 in rnn_dict.keys():
        if k2 in v:
            rnn_dict[k2].append(k)

e = time.time()
print('to get adj list for Reverse Nearest Neighbors: {}'.format(e-s))

output1 = rnn_dict

#save to csv
# with open('adj_list_RNN.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in output1.items():
#        writer.writerow([key, value])

e1 = time.time()
print('Calculate Nearest neighbor: {}'.format(e1-s1))



# Running time:

# load rankings and put in dict, with id as key and ranking list as value: 0.08147811889648438
# distance method for every single node against every other node: 459.90277099609375
# to get adj list for Nearest Neighbors: 0.09940075874328613
# to get adj list for Reverse Nearest Neighbors: 0.08702778816223145
# Calculate Nearest neighbor: 460.17084980010986
# Around 8 minutes for entire program.