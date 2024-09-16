def apply_all_func(int_list, *functions):
    res = {}
    for f in functions:
        res[f.__name__] = f(int_list)
    return res

lst= [6, 20, 15, 9]
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))