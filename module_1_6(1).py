#Работа со словарями:
my_dict = {'apple': 10, 'orange': 5, 'banana': 15}
print(my_dict)
print(my_dict['apple'])
print(my_dict.get('coconut'))
my_dict.update({'pear': 20, 'tangerine': 50})
print(my_dict)
del my_dict['apple']
print(my_dict)

#Работа с множествами:
my_set = {1, True, 'apple', 2.5, 1}
print(my_set)
my_set.add(5)
my_set.add((1, 2, 3))
print(my_set)
my_set.discard(1)
print(my_set)