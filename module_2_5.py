def get_matrix (n, m, value):

    matrix = []

    if n <= 0 or m <= 0:    #Проверка на некорректные размеры.
        return []

    for i in range(n):
        a = []              #Создаем новую строку.
        for i in range(m):
            a.append(value)
        matrix.append(a)

    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
