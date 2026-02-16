def loop3() :
    str = input("Enter a string consisting of digits , alphabets and special character : ")
    c = d = s = 0
    for ch in str:
        if ch.isdigit():
            d = d+1
        elif ch.isalpha():
            c = c+1
        else:
            s = s+1
    print("characters :",c,"digits :",d,"special character :",s)

loop3()
