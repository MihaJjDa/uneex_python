s = input()
d = {}
while s != "":
    for i in s.split(' '):
        if i != '':
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1

    s = input()

m = 0
s = '---'
for i, j in d.items():
    if j > m:
        m = j
        s = i
    elif j == m:
        m = j
        s = '---'
print(s)

