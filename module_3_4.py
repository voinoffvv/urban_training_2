def single_root_words(root_word = '', *other_words):
    res = list()
    for w in other_words:
        print(w)
    return res


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
#print(result1)
#print(result2)