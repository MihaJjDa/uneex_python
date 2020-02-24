a = eval(input())
Open = [0]
Closed = set()
fin = len(a)-1
while Open != []:
    k = Open.pop()
    if k == fin:
        Open = []
    else:
        Closed.add(k)    
        if not(k-1 in Closed) and k-1 >= 0:
            Open.append(k-1)
        if not(k+a[k] in Closed) and k+a[k] <= fin:
            Open.append(k+a[k])

print("YES") if k == fin else print("NO")
