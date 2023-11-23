# import numpy
# import pandas as pd
# import pyspark

# a = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(a)

# print(df) 

# # n first prime number

list_2D = [[1,2,4], [2,4,3], [0,0,1], [5,4,0]]
print(list_2D)
for row in list_2D:
    print(row)

list_row = []
list_col = []

for row in list_2D:
    list_row.append(sum(row))

print(list_row)
print(sum(list_row))

list_2D_transpose = []
tmp = []

for i in range(len(list_2D[0])):
    tmp = []
    tmp.append(list_2D[0][i])
    list_2D_transpose.append(tmp)

for i in range(1,len(list_2D)):
    for j in range(len(list_2D[i])):
        tmp = []
        tmp = list_2D_transpose[j]
        tmp.append(list_2D[i][j])
        list_2D_transpose[j] = tmp

for col in list_2D_transpose:
    list_col.append(sum(col))

print(list_col)
