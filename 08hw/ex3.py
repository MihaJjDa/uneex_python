s = input()
a = []
for i in s.split(' '):
    if i in ['+', '-', '*']:
        y = a.pop()
        x = a.pop()
        a.append(str(eval(x+i+y)))
    elif i.isnumeric() or (i[0] == '-' or i[0] == '+') and i[1:].isnumeric():
        a.append(i)
print(a.pop())
