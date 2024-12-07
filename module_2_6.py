def password(n):

    result = []

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            sum = i + j
            if n % sum == 0:
                result.append(f'{i}{j}')

    return ''.join(result)  #Метод строк, который используется для объединения элементов списка в одну строку.

print(password(5))
print(password(11))
print(password(20))