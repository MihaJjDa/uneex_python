from math import sin
a = eval(input())
a.sort(key = lambda x: sin(x))
print(a)
