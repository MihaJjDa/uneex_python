import math

def isnum(n):
    ok = True
    if n[0] == '-':
        i = 1
    else:
        i = 0
    while ok and i < len(n):
        ok = "0" <= n[i] <= "9"
        i += 1
    return ok

a = input()
max = -math.inf

while a != "":
    a = a.split(' ')
    for i in a:
        if isnum(i) and int(i) > max:
            max = int(i)
    a = input()

print(max)
