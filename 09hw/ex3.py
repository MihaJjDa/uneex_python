class Dots():
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
    def __getitem__(self, item):
        if type(item) == int:
            step = (self.b-self.a)/(item-1)
            return [self.a + i*step for i in range(item)]
        elif type(item) == slice:
            if item.step == None:
                step = (self.b-self.a)/(item.stop-1)
                return self.a + item.start*step
            else:
                if item.start == None:
                    start = 0
                else:
                    start = item.start
                if item.stop == None:
                    stop = item.step
                else:
                    stop = item.stop
                step = (self.b-self.a)/(item.step-1)
                return [self.a + i*step for i in range(start, stop)]
    def __del__(self):
        del self

"""
a = Dots(0,40)
print(*a[5])
print(a[0:5])
print(a[2:5])
print(a[4:5])
print(a[7:5])
print(a[-7:5])
print(*a[1:3:5])
print(*a[:3:5])
print(*a[2::5])
print(*a[::5])
print(*a[-2:6:5])
"""

