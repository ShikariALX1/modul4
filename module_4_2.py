def test_function():
    def inner_function():
        print(f'Я в области видимости функции test_function')

    inner_function()


test_function()
'''
inner_function() не вызвать вне функции, т.к. она находится внутри test_function()
и вызывать ее нужно внури соответственно.
'''
