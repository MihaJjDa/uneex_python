def num(a, n):
    return len([x for x in a if x % n == 0])

def moar(a, b, n):
    return num(a, n) > num(b, n)
