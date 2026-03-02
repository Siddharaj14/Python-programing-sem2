import operator
def tuple6() :
    fooditems = ('Potato','Cabbage','Tomato','Bhindi')
    print(fooditems)
    fi = input("Enter a food items : ")
    filist = []
    if fi in fooditems:
        newfi = input("Replace "+fi+" with what?")
        for i in fooditems:
            if i == fi:
                filist.append(newfi)
            else:
                filist.append(i)
        filist = tuple(filist)
    else:
        filist = fooditems
    print(filist)

tuple6()
    
