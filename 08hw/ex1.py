def toint(function):
    def fun(*args):
        nargs = (int(x) if type(x) == float else x for x in args)
        res = function(*nargs)
        res = int(res) if type(res) == float else res
        return res
    return fun 

"""
@toint
def root(x):
    return x**0.5
print(root(11.8))

@toint
def dou(x):
    return x*2

print(dou(11.8))
print(dou(11))
print(dou('11'))
print(dou((11,11)))
"""
