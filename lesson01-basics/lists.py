my_list = ['a', 'b', 'c', 1, 2, 3]

print(my_list)

print(my_list[2]) # -> c

my_list[2] = 'potato'
print(my_list) # -> ['a', 'b', 'potato', 1, 2, 3]

my_list.append('tomato')
print(my_list) # -> ['a', 'b', 'potato', 1, 2, 3, 'tomato']