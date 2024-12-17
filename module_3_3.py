def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

################################
# Вызываем функции с разными вариантами аргументов (1)
print_params()
print_params(10, 'клюква')
print_params(20, 'мох', 0)

print_params(b =63)
print_params(c=[1, 2, 3])

################################
# Распаковка параметров (2)
list_1 = [42, 'OMG', False]

dict_1 = {'a': 9.11, 'b': 'Абудефдуф', 'c': True}

print_params(*list_1)

print_params(**dict_1)

################################
# Распаковка + отдельные параметры (3)
list_2 = [23, 'stone']

print_params(*list_2, 32)