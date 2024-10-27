from pprint import pprint
import inspect


def introspection_info(obj):
    res = dict()
    res['Тип объекта'] = type(obj) # Тип объекта.
    res['Атрибуты объекта'] = dir(obj) # Атрибуты объекта.
    res['Методы объекта'] = list(filter(lambda arg: callable(getattr(obj, arg)), dir(obj)))
    res['Модуль'] = inspect.getmodule(type(obj))
    res['публичные Атрибуты'] = list(filter(lambda x: not x.startswith('_'), dir(obj)))
    return res

if __name__ == '__main__':
    number_info = introspection_info(42)
    pprint(number_info)
