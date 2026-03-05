import operator
def tuple5() :
    fooditems = (('Potato',30),(),('Cabbage',40),(),(),('Tomato',50),('Bhindi',100),())
    newfooditems = []
    for x in fooditems:
        if x:
            newfooditems.append(x)
    print(fooditems,newfooditems,sep='\n\n')
    
tuple5()

