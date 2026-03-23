def subjects() :
    s1 = {"Maths" , "Physics" , "Chemistry"}
    s2 = {"Physics" , "Biology" , "Maths"}
    a = s1.intersection(s2)
    b = s1.difference(s2)
    c = s2.difference(s1)
    d = c.union(b)
    print("Common subjects are :",a)
    print("Subjects tanken by only first student :",b)
    print("Subjects tanken by second first student :",c)
    print(len(d))

subjects()
