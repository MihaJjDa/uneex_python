def generator(a):
    yield -1*a
    yield str(a)
    yield abs(a) // 10 % 10
    
