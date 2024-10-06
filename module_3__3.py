def print_params(a=1, b='stroka', c=True):
    print(a, b, c)


print_params()
print_params(7, 'lower', False)
print_params(450, 'apple')
print_params(a ='params')
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [300, 'Windows', True]
values_dict = {'a': 999, 'b': 'modul', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# print_params(*values_list, **values_dict) - ошибка, так как, требуется больше элементов

values_list_2 = [66.4, 'swich']
print_params(*values_list_2, 2)
