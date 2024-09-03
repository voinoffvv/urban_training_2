# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
# Tакже переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __init__(self, name, number_of_floors):
        self.name = name
        #self.houses_history.append(name)
        self.number_of_floors = number_of_floors


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)