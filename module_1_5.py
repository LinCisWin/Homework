immutable_var = 1, True, "Зелень"
#immutable_var[0] = 2
#print(immutable_var) - будет ошибка. Кортеж предназначен,
# чтобы хранить данные, которые не нужно изменять
print(immutable_var)

mutable_list = [2, True, "Красный"]
print(mutable_list)
mutable_list[1] = False
print(mutable_list)