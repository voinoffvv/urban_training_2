# Создайте функцию read_info(name), где name - название файла. Функция должна:
# Создавать локальный список all_data.
# Открывать файл name для чтения.
# Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
# Во время считывания добавлять каждую строку в список all_data.
# Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
# Создайте список названий файлов в соответствии с названиями файлов архива.
# Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
# Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool.
# Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов.
# Измерьте время выполнения и выведите его в консоль.
import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        print(f'Читаем файл {name}')
        while True:
            st = f.readline()
            if not st:
                break
            all_data.append(st)
    print(f'Прочитано {len(all_data)} строк.')

if __name__ == '__main__':
    file_names = [f'file {i}.txt' for i in range(1, 5)]

    start_time = time.time()
    for file_name in file_names:
        read_info(file_name)
    print(f'Линейный подход - время {time.time() - start_time}')

    start_time = time.time()
    with Pool(len(file_names)) as p:
        res = p.map(read_info, file_names)
    print(f'Многопроцессный подход - время {time.time() - start_time}')
