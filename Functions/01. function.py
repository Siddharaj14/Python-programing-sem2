def count_lower_upper(st) :
    d = {'u':0 , 'l':0}
    for ch in st:
        if ch.isupper():
            d['u'] += 1
        else:
            d['l'] += 1
    return d
s = input("Enter a string : ")
print(s,count_lower_upper(s))
