i, j = eval(input())
d = {}
while (i, j) != (0, 0):
    if not(i in d.keys()):
        d[i] = set()
    if not(j in d.keys()):
        d[j] = set()
    d[i].add(j)
    d[j].add(i)
    i, j = eval(input())

s = []
m = len(d)-1
for i, j in d.items():
    k = len(j)
    if k == m:
        s += [i]

for i in sorted(s):
    print(i, end = ' ')
print()
