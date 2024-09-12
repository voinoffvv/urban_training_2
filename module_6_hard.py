import math

# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

class Figure():
    def __init__(self, color, sides_count):
        self.sides_count = sides_count
        self.__color = list(color)
        self.__sides = [1] * sides_count

    def __is_valid_color(self, new_color):
        return max(new_color) < 255 and min(new_color) > 0

    def get_color(self):
        return self.__color

    def set_color(self, r=0, g=0, b=0):
        new_color = [r, g, b]
        if self.__is_valid_color(new_color):
            self.__color = new_color

    def __is_valid_sides(self, new_sides):
        return len([x for x in new_sides if x <= 0 or type(x) != int]) == 0 and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = [*new_sides]

    def __len__(self):
        return sum(self.get_sides())


class Circle(Figure):
    def __init__(self, color, *args):
        super().__init__(color, 1)
        super().set_sides(*args)

    def __radius(self):
        s = super().get_sides()[0]
        return s / (2 * math.pi)

    def get_square(self):
        s = super().get_sides()[0]
        return s ** 2 / (4 * math.pi)


class Triangle(Figure):
    def __init__(self, color, *args):
        super().__init__(color, 3)
        super().set_sides(*args)

    def get_square(self):
        p = sum(self.get_sides()) / 2
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    def __init__(self, color, *args):
        super().__init__(color, 12)
        if len(args) == 1:
            super().set_sides(*args * 12)

    def get_volume(self):
        return self.get_sides()[0]*self.get_sides()[0]*self.get_sides()[0]

# testing...
if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15) # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    # cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    #Площадь треугольника
    triangle1 = Triangle((200, 200, 100), 2, 2, 2)  # (Цвет, стороны)
    print('Площадь треугольника = ', triangle1.get_square())