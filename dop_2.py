import random

res = list()
# res1 = list()
a = random.randint(3, 20)
for i in range(1, 21):
    for j in range(i + 1, 21):
        if a % (i + j) == 0:
            # res1.append([i, j])
            res.append(i)
            res.append(j)
print(f'{a}:', ''.join(str(c) for c in res1))
print(f'{a}:', ''.join(str(c) for c in res))
