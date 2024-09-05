class Animal:
    def __init__(self, name):
        self.alive = True  # живой
        self.fed = False  # накормленный
        self.name = name

        # Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.

    def eat(self, food):  # food - это параметр, принимающий объекты классов растений.
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:  # Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    edible = False # съедобность
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True # съедобность

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
