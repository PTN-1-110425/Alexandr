### Списки (List) / методы списков
# 1) Дан список чисел. Верни список, содержащий только уникальные элементы (встречающиеся один раз),
# в порядке их первого появления
# list1 = [4, 5, 2, 4, 3, 5, 2, 1]
# tmp = 0
# for i in list1:
#     if
#     print(i)

## 2) Напиши функцию, которая разбивает список на подсписки по n элементов
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = []
# list3 = []
# #list2[list2.append(i) for i in list1[0:3]]
# for i in list1[0:3]:
#     list2.append(i)
#
# print(list2)

#3) Выведите в отдельный список числа, которые меньше или равны 5 и числа, которые больше 5.

list1=[]
list2=[]
list3=[]
for i in range(0, 11):
    list1.append(i)
    if i <= 5:
        list2.append(i)
    else:
        list3.append(i)
print(list1)
print(list2)
print(list3)