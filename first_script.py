# x = float(input())
# y = float(input())
# z = float(input())

# sum3 = x + y + z

# print(sum3)

# sum15 = 0

# for i in range(0,15):
#     x = float(input())
#     sum15 += x

# print(sum15)

# n = int(input('Enter the number: '))

# sum_n = 0

# for i in range(0,n):
#     x = int(input())
#     sum_n += x

# print(sum_n)

# n = int(input('Enter the number: '))

# product_n = 1

# for i in range(0,n):
#     x = int(input())
#     product_n *= x

# print(product_n)

n = int(input('Number: '))
a = []

for i in range(0,n):
    x = int(input(f'Element number {i}: '))
    a.append(x)

def SimpleSearch(input_table, search_value):
    flag = 1
    for i in range(0,len(input_table)):
        if a[i] == search_value:
            print(str(i), end = ' ')
            flag = 0
    if flag == 1: print(-1)


k = int(input('Enter search number: '))
SimpleSearch(a,k)