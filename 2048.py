from random import randint
from random import choice
from os import system

def create_field(n):
    # create random field n * n

    arr = []
    for i in range(n):
        arr.append([])
        for j in range(n):
            arr[i].append(0)
    return arr

def fill_slot(field):
    # fill random empty slot
    if is_step(field) != False:
        coord = choice(is_step(field))
        field[coord[0]][coord[1]] = two_or_four()
        return field
    else:
        return False

def two_or_four():
    # 90 per = return 4, 10 per = return 2

    if randint(1, 10) == 10:
        return 4
    return 2

def is_step(field):
    li = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 0:
                li.append([i,j])
    if not li:
        return False

    return li

def get_size():
    # set field size n * n
    q = ' <<< Set your side for game field \n' \
        'your number must be more than or equal 3 >>> '
    n = 0
    while n < 3:
        n = int(raw_input(q))
    return n

def start_game():
    # get size
    size = get_size()

    # create field
    field = create_field(size)

    # first_fill_slot
    fill_slot(field)
    fill_slot(field)

    # show field
    show_field(field)

    # start game
    game(field)

def show_field(field):
    system('clear')
    print '<---------->'
    for i in field:
        print i
    print '<---------->'

def move(field, move='up'):

    if move == 'down':
        field = field[::-1]
    elif move == 'left':
        field = turn_right(field)
    elif move == 'right':
        field = turn_left(field)

    for i in range(len(field)):
        point = 0
        j = 1

        while j < len(field):
            if field[j][i] == 0:
                j += 1
            elif field[point][i] == 0:
                field[point][i] = field[j][i]
                field[j][i] = 0
                j += 1
            elif field[point][i] == field[j][i]:
                field[point][i] *= 2
                field[j][i] = 0
                j += 1
                point += 1
            else:
                if abs(j - point) != 1:
                    point += 1
                else:
                    point += 1
                    j += 1

    if move == 'down':
        field = field[::-1]
    elif move == 'left':
        field = turn_left(field)
    elif move == 'right':
        field = turn_right(field)

    return field

def game(field):

    while True:
        old_field = []
        for i in field:
            old_field.append(i[:])
        field = action(get_side(), field)
        if old_field == field and is_step(field) != False:
            continue
        if fill_slot(field) == False:
            print '<=============>'
            print '{:^15}'.format('Game Over')
            print '<=============>'
            break
        show_field(field)

def action(x, field):
    if x == 'w':
        return move(field)
    elif x == 'a':
        return move(field, 'left')
    elif x == 's':
        return move(field, 'down')
    elif x == 'd':
        return move(field, 'right')

def turn_left(field):
    arr = [[0] * (len(field)) for k in range(len(field))]

    for i in range(len(field)):
        for j in range(len(field)):
            arr[len(field) - 1 - j][i] = field[i][j]

    return arr

def turn_right(field):
    arr = [[0] * (len(field)) for k in range(len(field))]

    for i in range(len(field)):
        for j in range(len(field)):
            arr[i][j] = field[len(field) - 1 - j][i]

    return arr

def get_side():
    res = 'nope'
    while res.strip() not in ('w', 'a', 's', 'd'):
        res = raw_input(' \n Pls choice a action (type: \n' \
                        '\'w\' for UP, \'a\' for RIGHT, \'s\' for DOWN, \'d\' for WEST) >>> ')
    else:
        return res.strip()

start_game()
