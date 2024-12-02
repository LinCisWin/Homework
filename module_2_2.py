first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

# Проверяем условия.
if first == second == third:
    print(3)                                                    # Все числа равны
elif first == second or first == third or second == third:
    print(2)                                                    # Два из трёх числа равны
else:
    print(0)                                                    # Равных чисел нет