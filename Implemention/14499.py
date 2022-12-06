def roll_dice(roll):
    a,b,c,d,e,f =dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    return({1:[d, b, a, f, e, c],2:[c, b, f, a, e, d],3:[e, a, c, d, f, b],4:[b, f, c, d, a, e]}.get(roll))


n, m, x, y, k = map(int, input().split(' '))
my_map = []
dice = [0,0,0,0,0,0]

for i in range(n):
    my_map.append(list(map(int, input().split(' '))))

direction = list(map(int, input().split(' ')))

for i in direction:
    if my_map[x][y] == 0:
        my_map[x][y] = dice[5]
    else:
        dice[5]= my_map[x][y]

    nx,ny={1: [x, y + 1], 2: [x, y - 1], 3: [x - 1, y], 4: [x + 1, y]}.get(i)
    if nx <0 or ny <0:
        continue
    # if nx>m or ny>n:
    #     continue
    else:
        dice = roll_dice(i)
        x,y = nx,ny

    print(dice[0])