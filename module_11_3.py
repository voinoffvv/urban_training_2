from pprint import pprint
import inspect

class MyClass(object):
    def __init__(self):
        self.attr1 = 10
        self.name= 'MyClass !!!'

    def fu1(self):
        return self.attr1 * 2

    def __str__(self):
        return self.name


def introspection_info(obj):
    res = dict()
    res['Тип объекта'] = type(obj) # Тип объекта.
    res['Атрибуты объекта'] = dir(obj) # Атрибуты объекта.
    res['Методы объекта'] = list(filter(lambda arg: callable(getattr(obj, arg)), dir(obj)))
    res['Модуль'] = inspect.getmodule(type(obj))
    res['публичные Атрибуты'] = list(filter(lambda x: not x.startswith('_'), dir(obj)))
    return res

if __name__ == '__main__':
    myClassObj = MyClass()
    number_info = introspection_info(myClassObj)
    pprint(number_info)
