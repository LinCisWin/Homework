grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#Преобразуем в отсортированный список множество студентов.
sorted_students = sorted(students)

#Создаём словарь (ключ - имя, значение - средний балл).
average_grades = {
    student: sum(grades[i]) / len(grades[i])        #Средний бал каждого ученика
    for i, student in enumerate(sorted_students)    #Цикл, который перебирает имена учеников и их соответствующие индексы
}
#Выводим результат
print(average_grades)