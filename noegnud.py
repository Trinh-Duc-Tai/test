from random import randint

horizontal_dash = '-'
player = 'P'
key = 'K'
escape = 'E'
m1 = 4
n1 = 4
xp = randint(0, 3)
yp = randint(0, 3)
xe = randint(0, 3)
ye = randint(0, 3)
xk = randint(0, 3)
yk = randint(0, 3)
v_x = 1
v_y = 1

k1  = False

def show_map():
    for i in range(m1):
        for j in range(n1):
            if j == xp and i == yp:
                print(player, end = ' ')
            elif j == xk and i == yk:
                if k1 == False :
                    print(key, end = ' ')
                else:
                    print(horizontal_dash, end = " ")
            elif j == xe and i == ye:
                print(escape, end = ' ' )
            else:
                print(horizontal_dash, end = ' ')
        print()

while True:
    xp = randint(0, 3)
    yp = randint(0, 3)
    xe = randint(0, 3)
    ye = randint(0, 3)
    xk = randint(0, 3)
    yk = randint(0, 3)
    if not ((xp == xe) and (yp == ye) or (xp == xk) and (yp == yk) or (xe == xk) and (ye == yk)):
        break

while True:
    show_map()
    output = input('Your move: ').lower()
    if  output == "d":
        xp += v_x
        if xp > 3 :
            xp -= v_x
            print('Out of map, please try again')
    elif output == 'a':
        xp -= v_x
        if xp < 0 :
            xp += v_x
            print('Out of map, please try again')
    elif output == 'w':
        yp -= v_y
        if yp <0 :
            yp += v_y
            print('Out of map, please try again')
    elif output == 's':
        yp += v_y
        if yp > 3 :
            yp =- v_y
            print('Out of map, please try again')
    if xp == xk and yp == yk:
        print('You’ve just picked up a key!!!')
        k1 = True
    if xp == xe:
        if yp == ye:
            if k1 == True :
                show_map()
                print('Congrats, you’ve just escaped the dungeon')
                break    
            else:
                print("You can't exit, please acquire the key(s) first")    