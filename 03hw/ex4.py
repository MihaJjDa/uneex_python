def GCD(a, b):
    if a == b:
        return a
    else:
        a -= b
        if a >= b:
            return GCD(a, b)
        else:
            return GCD(b, a)

a,b = eval(input())
res = ""
if a//b != 0:
    res += str(a//b)
if a//b != 0 and a % b != 0:
    res += " "
if a % b != 0:
    a = a % b
    mod1 = a // GCD(b, a)
    mod2 = b // GCD(b, a)
    res += str(mod1) + "/" + str(mod2)
print(res)

