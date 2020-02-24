class LetterAttr():
    def __init__(self):
        pass
    def __getattr__(self, a):
        self.__setattr__(a, a)
        return a
    def __setattr__(self, a, b):
        b = [x for x in b if x in a]
        super().__setattr__(a, ''.join(b))
'''
A = LetterAttr()
print(A.letter)
print(A.digit)
A.letter = 'teller'
print(A.letter)
A.letter = 'fortune teller'
print(A.letter)
'''

