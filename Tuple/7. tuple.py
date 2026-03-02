import operator
def tuple7() :
    fooditems = ('Potato','Cabbage','Tomato','Bhindi')
    print(fooditems)
    fi = input("Enter a food item to be deleted : ")
    filist = []
    if fi in fooditems:
        for i in fooditems:
            if i != fi:
                filist.append(i)
        filist = tuple(filist)
    else:
        filist = fooditems
    print(filist)

tuple7()
