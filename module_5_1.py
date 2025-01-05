def test_function():

    def inner_function():

        print("Я в области видимости функции test_function")

    inner_function()

test_function()

#def inner_function():
#   print('ok')

if 'inner_function' in globals():
    inner_function()
else:
    print('inner_function не определена в глобальной области')