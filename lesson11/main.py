
### Тема: *args и **kwargs / lamda, (zip, map, filter)
'''
1) Создайте функцию print_info, которая принимает произвольное количество именованных аргументов
 и печатает их в виде «ключ: значение».
'''
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key + ':', value)
#
# print_info(name='Иван', age='30', country='Казахстан')

'''
2) Создайте функцию custom_filter, которая принимает: неограниченное количество именованных условий через **kwargs.
 Функция должна возвращать новый список, отфильтрованный по условиям. список элементов первым аргументом
'''
# def custom_filter(**kwargs):
#     #itms = kwargs
#     filtered = [filter(custom_filter, kwargs)]
#     for key, value in kwargs.items():
#         print(f'Ключ: {key}')
#         print(f'Значение: {value}\n')
#
#     print(filtered)
#
# custom_filter(name='IPhone', brand='Apple', price=1000)