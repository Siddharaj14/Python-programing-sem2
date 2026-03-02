import operator
def tuple4() :
    fooditems = [('Potato',30) , ('Cabbage',40) , ('Tomato',50) , ('Bhindi',100)]
    sortedfooditems = sorted(fooditems,key=operator.itemgetter(1),reverse=True)
    print(sortedfooditems)

tuple4()
    
    
    
