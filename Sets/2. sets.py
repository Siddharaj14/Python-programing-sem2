def visitors() :
    d1 = {130,121,71}
    d2 = {126,102,71}
    a = d1.intersection(d2)
    b = d1.symmetric_difference(d2)
    c = d1 | d2
    print("Students visited both the days are :",a)
    print("Students visited only one of the days are :",b)
    print("Total unique visitors are :",len(c))

visitors()
