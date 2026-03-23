import random
def duplicate() :
    lst = [random.randrange(-5,5) for x in range(15)]
    print(lst)
    uniquelst = list(set(lst))
    print(uniquelst)

duplicate()
