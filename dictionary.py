#данные в словаре это пара ключ значение
my_dict={'one':'value','two':'value2','three':3}
print(my_dict['one'])
print(len(my_dict))
my_dict['one']='val'
my_dict['four']='value4'
my_dict['five']= [1, 6 ,8]
my_dict['six']= {1, 2, 3}
my_dict[7]= 'lol'
my_dict[4.21]= 'val11'
print(my_dict['one'])
print(my_dict)

#вывод только ключа или значения
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dic3={} #это пустой словарь