class Animal:
    alive = True # живой
    fed = False # накормленный
    def __init__(self, name):
        self.name = name

        # Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.

    def eat(self, food):  # food - это параметр, принимающий объекты классов растений.
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            self.alive = True
        else:  # Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
            print(f'{self.name} не стал есть {food.name}')
            self.fed = False
            self.alive = False

class Plant:
    edible = False # съедобность
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name):
        self.name = name

class Predator(Animal):
    def __init__(self, name):
        self.name = name

class Flower:
    edible = False # съедобность
    def __init__(self, name):
        self.name = name
class Fruit:
    edible = True # съедобность
    def __init__(self, name):
        self.name = name

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
