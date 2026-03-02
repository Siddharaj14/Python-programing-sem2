def tuple1() :
    stud_names = ['Anurakti' , ('Datt',) , 'Meswa' , ('Shivom','Jahan')]
    b = g = 0
    for s in stud_names:
        if isinstance(s,tuple):
            b = b + len(s)
        else:
            g = g + 1
    print(stud_names,b,g)
tuple1()
