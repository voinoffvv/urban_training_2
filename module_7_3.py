import os
class WordsFinder():
    def __init__(self, *args):
        self.file_names = args
    def get_all_words(self):
        res = {}
        for fname in self.file_names:
            if os.path.exists(fname):
                with open(fname, 'r', encoding="utf-8") as file:
                    s = file.read().lower()
                    for i in [',', '.', '=', '!', '?', ';', ':', ' - '] :
                        s = s.replace(i, '')
                    s = s.replace('\n', ' ')
                    res[fname] = s.split(' ')
                    file.close()
        return res

    def find(self, word:str)->dict:
        res = {}
        s = self.get_all_words()
        for k in s.keys():
            i = 1
            for sl in s.get(k):
                if sl == word.lower():
                    res[k] = i
                    break
                i += 1
            # try:
            #     res[k] = s.get(k).index(word.lower()) + 1
            # except:
            #     pass
        return res
    def count(self, word:str)->dict:
        res = {}
        s = self.get_all_words()
        for k in s.keys():
            i = 0
            for sl in s.get(k):
                if sl == word.lower():
                    i += 1
            if i > 0:
                res[k] = i
        return res

    def create_test_file(self):
        a = {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
        with open(*a.keys(), 'w', encoding="utf-8") as file:
            file.write(' '.join(a.get(*a.keys())))
            file.close()

finder2 = WordsFinder('test_file.txt', 'products1.txt', 'test1.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего