m, n = eval(input())
u, l = 0, 0
d, r = n-1, m-1
a = [[10 for x in range(m)] for x in range(n)]
t, i, j, dr = 0, 0, 0, 0
#print(a)
while (i in list(range(n))) and (j in list(range(m))) and a[i][j] == 10:
#    print(t)
    a[i][j] = t
    t = (t + 1) % 10
#    print("1 DIR", dr, "U", u, "D", d, "L", l, "R", r, "i", i, "j", j)
    if dr == 0:
        if j == r and i != d:
            i += 1
            dr = 1
            u += 1
#        elif j == r and 
        else:
            j += 1
    elif dr == 1:
        if i == d and j != l:
            j -= 1
            dr = 2
            r -= 1
        else:
            i += 1
    elif dr == 2:
        if j == l and i != u:
            i -= 1
            dr = 3
            d -= 1
        else:
            j -= 1
    elif dr == 3:
        if i == u and j != r:
            j += 1
            dr = 0
            l += 1
        else:
            i -= 1
#    print("  DIR", dr, "U", u, "D", d, "L", l, "R", r, "i", i, "j", j)
#print(a)
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ') if j != m-1 else print(a[i][j])
