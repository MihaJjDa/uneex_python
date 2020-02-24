def f(x0, y0, r):
    x, y = eval(input())
    if (x == 0) and (y == 0):
        return "YES"
    elif (x-x0)**2 + (y-y0)**2 > r*r:
        return "NO"
    else:
        return f(x0, y0, r)


x0, y0, r = eval(input())
print(f(x0, y0, r))
