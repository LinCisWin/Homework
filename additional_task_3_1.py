
def calculate_structure_sum(data):
    total = 0   # Переменная для хранения общей суммы

    if isinstance(data, (list, tuple, set)):    # Если список, котеж или множество
        for item in data:
            total += calculate_structure_sum(item)
    elif isinstance(data, dict): # Если словарь
        for key, value in data.items():
            total += calculate_structure_sum(key)   # Ключ
            total += calculate_structure_sum(value) # Значение
    elif isinstance(data, (int, float)):    #Если число
        total += data
    elif isinstance(data, str): # Если строка
        total += len(data)

    return total


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]



result = calculate_structure_sum(data_structure)
print(result)