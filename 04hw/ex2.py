import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

a = eval(input())
ok = False
while not ok and a > 2:
    ok = is_prime(a)
    a -= 1
print(a+1)
    
    
        
