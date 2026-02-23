import random
def list3() :
    lst = [random.randrange(1,30) for x in range(50)]
    print(lst)
    newlst = []
    for v in lst:
        if v not in newlst:
            newlst.append(v)
    print(newlst)

list3()
