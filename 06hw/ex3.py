def squares(w, h, *sq):
    screen = [['.' for i in range(w)] for i in range(h)]
    for s in sq:
        j1, i1 = s[0], s[1]
        for i in range(i1, i1+s[2]):
            for j in range(j1, j1+s[2]):
                screen[i][j] = s[3]
    for i in range(h):
        for j in range(w):
            print(screen[i][j], end="")
        print()

