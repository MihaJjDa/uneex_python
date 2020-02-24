s = input()
a = input()

i = 0
ok = False
if len(a) <= len(s):
    while not ok and i < len(s):
        if s[i] == a[0] or a[0] == '@':
            j = 1
            ok = True
            while ok and j < len(a):
                ok = a[j] == '@' or (i+j < len(s) and a[j] == s[i+j])
                j += 1
        i += 1

if ok:
    print(i-1)
else:
    print(-1)
