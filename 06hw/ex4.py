a = input().lower().split(" ")
b = input().lower().split(" ")

tmp = []
for i, l in enumerate(a):
    for j in l:
        if not j.isalpha():
            a[i] = a[i][:-1]
            tmp += [j]
a += tmp

tmp = []
for i, l in enumerate(b):
    for j in l:
        if not j.isalpha():
            b[i] = b[i][:-1]
            tmp += [j]
b += tmp

print(sorted(a) == sorted(b))
        

