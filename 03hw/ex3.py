def e(x):
    if x <= 9:
        return 1
    else:
        return 10 * e(x//10)

def f(x):
    if x <= 9:
        return True
    else:
        a = x % 10
        b = e(x)
        c = x // b
        return (a == c) and f((x % b)//10)

a = eval(input())
if f(a):
    print("YES")
else:
    print("NO")
