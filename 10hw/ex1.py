class DivStr(str):
    def __floordiv__(self, b):
        div = [self[x:x+len(self)//b] for x in range(0, len(self), len(self)//b)]
        return div[:-1] if len(div[-1]) < b else div
    def __mod__(self, b):
        div = [self[x:x+len(self)//b] for x in range(0, len(self), len(self)//b)]
        return div[-1] if len(div[-1]) < b else ''

'''
a = DivStr("12345678901234567")
print(a)
print(*a//4)
print(a%4)
'''

