def konv(k):
    tmp = ""
    x = str(k)[0]
    n = 0
    for i in str(k):
        if i == x:
            n += 1
        else:
            tmp = tmp + str(n) + str(x)
            n = 1
            x = i 
    tmp = tmp + str(n) + str(x)
    return int(tmp)
                
        

def LookSay():
    k = 1
    s = ""
    while True:
        if s == "":
            s = str(k)
            k = konv(k)
        yield int(s[0])
        s = s[1:]
    
