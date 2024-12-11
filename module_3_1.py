calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()   #Увеличиваем счетчик вызовов
    return len(string), string.upper(), string.lower() #Длина, верхний регистр, нижний регистр

def is_contains(string, list_to_search):
    count_calls()   #Увеличиваем счетчик вызовов
    string_lower = string.lower()   #Приводим строку к нижнему регистру
    list_lower = [item.lower() for item in list_to_search]  #Приводим все эелементы к нижнему регистру
    return string_lower in list_lower   #Проверяем наличие строки в списке

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)    #Вывод общего количества