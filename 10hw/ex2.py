import collections

class DefCounter(collections.Counter):
    def __init__(*args, missing=-1, **kwds):
        self, *args = args
        super(collections.Counter, self).__init__()
        self.update(*args, **kwds)
        self.missing = missing
    def __missing__(self, key):
        return self.missing

'''    
A = DefCounter("QWEqweQWEqweQWE", missing=-10)
print(A)
print(A["Z"])
A["P"]+=5
print(A)
'''

