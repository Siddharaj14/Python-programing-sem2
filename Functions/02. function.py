def count(n) :
    s = t = 0
    for i in range(4):
        t = t*10 + n
        s = s + t
    return s

##for v in range(4,8):
##    print(v,count(v))
