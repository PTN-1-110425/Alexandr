###  Водная информация по функциям
##  Урок десятый, домашнее задание №1
'''
1) Напишите функцию, чтобы найти максимальное из трех чисел
'''
# def max_num(a: int, b: int, c: int)-> int:
#     m_n = 0
#     if a > b and a > c:
#         m_n = a
#     elif b > a and b > c:
#         m_n = b
#     elif c > a and c > b:
#         m_n = c
#     return m_n
#
# #a, b, c = int(input('Введите через пробел три целочисленных значения: ').split())
# print(max_num(12, 15, 7))

'''
2) Напишите функцию, для суммирования всех чисел в списке. Не использовать встроенную функцию sum()
Образец списка: (8, 2, 3, 0, 7)
'''

# def num_sum(*args: int)-> int:
#     list1 = [*args]
#     cnt = 0
#     for i in list1:
#         cnt += i
#     return cnt
#
# print(num_sum(12,77,435,122,15,10,11))

'''
3) Напишите функцию, для умножения всех чисел в спискe друг на друга
'''
# def mult_num(*args: int)-> int:
#     list1 = [*args]
#     cnt = 1
#     for i in list1:
#         cnt *= i
#     return cnt
#
# print(mult_num(2, 3, 1, 5, 0))

'''
4) Напишите функцию, для переворота строки без использования встроенных функций
'''
# def revers_list(*args)-> list:
#     list1 = [*args]
#     list2 = list1[-1:-(len(list1)+1):-1]
#     return list2
#
# print(revers_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def revers_list(*args):
#     list1 = [*args]
#     list2 = [i for i in list1[::-1]]
#     return list2
#
# print(revers_list(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0))

'''
5) Напишите функцию, для вычисления факториала числа (Натуральное число).
Функция принимает число в качестве аргумента
'''

'''
6) Напишите функцию, которая принимает строку и вычисляет количество букв верхнего и нижнего регистра
'''
# def upper_lower_num(*args: str)-> str:
#     str1 = [*args]
#     #print(str1)
#     upper_cnt = 0
#     lower_cnt = 0
#     for i in str(str1):
#         if i.isupper():
#             upper_cnt += 1
#         elif i.islower():
#             lower_cnt += 1
#     return (f'Кол-во символов в нижнем регистре: {lower_cnt}\n'
#             f'Кол-во символов в верхнем регистре: {upper_cnt}')
#
# print(upper_lower_num('ЗахватИ ЗонТиК'))

'''
7) Напишите функцию, которая принимает слово и определяет является ли оно палиндромом
(палиндром — Слово или фраза, которые одинаково читаются слева направо и справа налево.)
'''
# def palindrom_str(*args):
#     list1 = [*args]
#     str1 = ''
#     str1 = ''.join( list1)
#     print(str1)
# if str1[::] == str1[::-1]:
#     print('YES', str1[::], str1[::-1])
# else:
#     print('NO', str1[::], str1[::-1])

palindrom_str('щтщ')
# st = 'ovo'
# list1 = [st]
# print(list1)
# str1 = ''
# str1 = ''.join(list1)
# print(str1)