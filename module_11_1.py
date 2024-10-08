# Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
# После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями.
# К каждой библиотеке дана ссылка на документацию ниже.
# Если вы выбрали:
# requests - запросить данные с сайта и вывести их в консоль.
# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
# matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
# pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.

import time
import requests
import pandas
import numpy

print('############################      requests      ###########################################')
payload = {'key1': 'value1', 'key2': 'value2'}
r1 = requests.get('https://httpbin.org/get', params=payload)
print('json = ', r1.json())
print('text = ', r1.text)
print('url = ', r1.url)
print('encoding = ', r1.encoding)
print('request.method = ', r1.request.method)
print('content = ', r1.content)

print('############################      pandas      ###########################################')
# Скачаем файл для работы и сохраним его
dict1 = {'apples': [4,5,8,8,9,8],'bananas': [1,2,3,4,5,6],'oranges': [3,4,2,4,9,6]}
file_name = 'data.csv'
t = requests.get('https://raw.githubusercontent.com/voinoffvv/urban_training_2/refs/heads/main/data1.csv').text
with open(file_name, 'w', encoding='utf-8', newline='\n') as file:
    for s in t.splitlines():
        file.write(s + '\n')
    file.close()
data = pandas.read_csv(file_name) # Читаем данные из файла
if data.empty: data = pandas.DataFrame(dict1)
print(data)
print('******* apples ********\n', data['apples']) # выбор по столбцам
data['TOTAL'] = data['apples'] + data['bananas'] + data['oranges'] # Добавляем итоги по строкам
print(data[1:3]) # срез по индексам
print(data.describe()) # сводная по столбцам
pur2 = data[data['TOTAL'] > 10] # фильтрация
print(pur2)
data.to_excel('data.xlsx', sheet_name='Sheet1', index=False) # сохранить в файл excel

print('############################      numpy      ###########################################')
print('создали пустой массив\n', numpy.empty((2,3))) # создали пустой массив
print('создали массив из словаря\n', numpy.array(list(dict1.values()))) # создали массив из словаря

print('Транспонировали его\n', numpy.array(list(dict1.values())).T) #Транспонирование

np_data = numpy.arange(24).reshape(2,3,4) # трехмерный массив
print('трехмерный массив\n', np_data)
print('Сумма всех элементов массива\n', np_data.sum())
print('Выбор четных значений элементов\n', np_data[np_data % 2 == 0])

a1 = numpy.arange(0, 5)
a2 = a1.copy()
print('Сумма двух массивов\n', a1 + a2)
numpy.savetxt('new_file.csv', a1 + a2) # Сохраним в файл
#
#
