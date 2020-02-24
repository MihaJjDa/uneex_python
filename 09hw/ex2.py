class vector():
    def __init__(self, a):
        self.body = [x for x in a]
    def __add__(self, a):
        tmp = vector([x+y for x,y in zip(self.body,a)])
        return tmp
    def __radd__(self, a):
        tmp = vector([x+y for x,y in zip(self.body,a)])
        return tmp
    def __getitem__(self, i):
        return self.body[i]
    def __str__(self):
        s = ""
        for i in self:
            s += str(i) + ':'
        return s[:-1]
    def __del__(self):
        del self
"""
a, b = vector([2,1,2,1,2,1,2,1]), vector(range(8))
print(a, b, a+b, b+range(8), range(8)+b)
"""
