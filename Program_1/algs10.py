from algs9_1 import matthewGraph
from algs6 import plot
import csv
import ast

#average outdegree of canvas dataset
#d = 12.703204897371265 so round up to 13
d = 13
matt = matthewGraph(d, 27770)
plot(matt)


#save to csv
with open('alg_10.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in matt.items():
       writer.writerow([key, value])











