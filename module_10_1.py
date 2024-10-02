# Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла,
# куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

from threading import Thread
from time import sleep
from datetime import datetime

def write_words (word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)
        f.write(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()
times = (10,30,200,100)
file_num = 1
threads = []
for n in times:
    write_words(n, f'example{file_num}.txt')
    thread = Thread(target=write_words, args=(n, f'example{file_num + len(times)}.txt'))
    threads.append(thread)
    file_num += 1

time_end = datetime.now()
print(f'Время без потоков {time_end - time_start}')

time_start = datetime.now()
for t in threads:
    t.start()
for t in threads:
    t.join()
time_end = datetime.now()
print(f'Время с потоками {time_end - time_start}')

# Время без потоков 0:00:34.138871
# Время с потоками 0:00:20.080455
