import random
def addlist3() :
    l1 = [random.randrange(-15,15) for x in range(10)]
    print(l1)
    l2 = list(map(lambda x : x*x,l1))
    print(l2)

addlist3()
