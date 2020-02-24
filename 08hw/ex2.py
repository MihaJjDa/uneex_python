def turtle(coord, direction):
    coord = list(coord)
    act = yield coord
    while True:
        if act == 'f':
            if direction == 0:
                coord[0] += 1
            elif direction == 1:
                coord[1] += 1
            elif direction == 2:
                coord[0] -= 1
            elif direction == 3:
                coord[1] -= 1
        elif act == 'l':
            if direction == 0:
                direction = 1
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 3
            elif direction == 3:
                direction = 0
        elif act == 'r':
            if direction == 0:
                direction = 3
            elif direction == 1:
                direction = 0
            elif direction == 2:
                direction = 1
            elif direction == 3:
                direction = 2
        act = yield coord
"""
robo = turtle((0,0),0)
start = next(robo)
for c in "flfrffrffr":
    print(*robo.send(c))
"""
