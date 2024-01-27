def my_func(a, list1=[]):
    return list1.append(a)

l = my_func('3')
l = my_func('4')
l = my_func('a')
print(l)