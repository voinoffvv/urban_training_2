# a = [['00', '01', '02'],
#      ['10', '11', '12'],
#      ['20', '21', '22']]

def check_winner():
    for i in range(0,3):
        r = set(area[i])
        c = {area[0][i], area[1][i], area[2][i]}
        if len(r) == 1:
            return r.pop()
        if len(c) == 1:
            return c.pop()
    x1 = {area[0][0], area[1][1], area[2][2]}
    if len(x1) == 1:
        return x1.pop()
    x2 = {area[2][0], area[1][1], area[0][2]}
    if len(x2) == 1:
        return x2.pop()
    return '*'

def draw_are():
    for i in area:
        print(i)
    print()

#area = [['*'] * 3] * 3
area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('______________________________________________')
draw_are()
for i in range(1,10):
    print('Ход', i)
    if i % 2 == 0:
        t_char = '0'
        print('Ходят нолики')
    else:
        t_char = 'X'
        print('Ходят крестики')
    row = int(input('row: ')) - 1
    col = int(input('col: ')) - 1
    if area[row][col] == '*':
        area[row][col] = t_char
    else:
        print('Ячейка занята. Пропуск хода.')
        draw_are()
    draw_are()
print('Победителем является:', check_winner())

