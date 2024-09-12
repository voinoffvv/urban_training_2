import os

class Product():
    def __init__(self, name, weight, category ):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        res = ''
        if os.path.exists(self.__file_name):
            with open(self.__file_name, 'r') as file:
                res = file.read()
                file.close()
        return res

    def add(self, *products):
        lst = self.get_products().split('\n')
        with open(self.__file_name, 'a') as file:
            for p in products:
                if str(p) not in lst:
                    file.write(str(p)+'\n')
                else:
                    print(f'{p} уже есть в магазине.')
            file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


