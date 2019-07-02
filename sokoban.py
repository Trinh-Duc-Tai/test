from random import randint

x = 4
y = 4
player = 'P'
box = 'B'
storage_point = 'S'
horizontal_dash = '-'

while True:
    xp = randint(0,3)
    yp = randint(0,3)
    xb = randint(1,2)
    yb = randint(1,2)
    xs = randint(0,3)
    ys = randint(0,3)
    if not ((xp == xb) and (yp == yb) or (xp == xs) and (yp == ys) or (xb == xs) and (yb == ys)):
        break

def show_map(): 
    for i in range(x):
        for j in range(y):
            if j == xp and i == yp:
                print(player, end=' ')
            elif j == xb and i == yb:
                print(box, end=' ')
            elif j == xs and i == ys:
                print(storage_point, end=' ')
            else: 
                print(horizontal_dash, end=' ')
        print()

while True: 
    show_map()
    output = input('Your move ?').lower()
    if output == 'd':
        xp += 1
        if xp > 3:
            xp -= 1
            print('Out of map, please try again')
        if xp == xb and yp == yb :
            xb += 1
            if xb > 3:
                xp -= 1
                xb -= 1
                print('A box is out of map')
    elif output == 's':
        yp += 1
        if yp > 3: 
            yp -= 1
            print('Out of map, please try again')
        if xp == xb and yp == yb:
            yb += 1
            if yb > 3:
                yp -= 1
                yb -= 1
                print('A box is out of map')
    elif output == 'a':
        xp -= 1
        if xp < 0:
            xp += 1
            print('Out of map, please try again')
        if xp == xb and yp == yb: 
            xb -= 1
            if xb < 0:
                xp += 1
                xb += 1
                print('A box is out of map')
    elif output == 'w':
        yp -= 1
        if yp < 0:
            yp += 1
            print('Out of map, please try again')
        if xp == xb and yp == yb:
            yb -= 1
            if yb < 0:
                yp += 1
                yb += 1
                print('A box is out of map')
    if xb == xs and yb == ys:
        show_map()
        print("You've won !!!")
        break
    