import random
def list4() :
    lst = [random.randrange(-30,30) for x in range(30)]
    nlst = [v for v in lst if v < 0]
    plst = [v for v in lst if v > 0]
    print(lst,nlst,plst,sep="\n")

list4()
