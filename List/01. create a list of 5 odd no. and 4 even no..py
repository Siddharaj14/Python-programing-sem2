import random
def list1() :
    odd = [random.randrange(1,100,2) for x in range(5)]
    even = [random.randrange(2,100,2) for x in range(4)]
    print("Odd Numbers :",odd)
    print("Even Numbers :",even)
    odd[2] = even
    print("Odd number updated :",odd)
    newlist = []
    for v in odd:
        if type(v) == int:
            newlist.append(v)
        else:
            newlist.extend(v)
    print("Flatterned List :",newlist)
    newlist.sort()                                                                                                                                                                                                                                                                                                                                                                                                                  
    sortednewlist = sorted(newlist,reverse = True)
    print("Sorted List :",newlist)
    print("New Sorted List :",sortednewlist)

list1()
    
