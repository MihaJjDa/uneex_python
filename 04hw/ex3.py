from math import inf

a = eval(input())

m1, m2 = -inf, -inf

for i in a:
    if i > m1:
        m2, m1 = m1, i
    elif i != m1 and i > m2:
        m2 = i

if m2 > -inf:
    print(m2)
else:
    print("NO")
    
