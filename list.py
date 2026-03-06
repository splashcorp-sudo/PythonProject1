#list
my_list = [1, 3, 6, 'text', False]
print(my_list[2])
print(my_list[-1])
my_list[4] = 42
print(my_list)

my_list2=[] #создали пустой лист
my_list2.append(42) #добавили данные в лист лист
my_list2.append('kek') #добавили данные в лист лист
my_list2.append('3') #добавили данные в лист лист
print(my_list2)
print(len(my_list2)) #посчитали количество элементов в листе
print(my_list2.index('kek')) #найти индекс где расположен кек (1 так как начинаем считать с нуля)
my_list2.pop(0) #удалить элемент под индексом 0 (42)
poped=my_list2.pop(0) #удалить элемент под индексом 0
print(poped)# и отобразить что конкретно удалили
print(my_list2)
print('3' in my_list2) #проверить '3' в списке


my_list3=list() #создали пустой лист, другой вариант

#преобразовать лист в сет
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
data=set(data)
print(data)