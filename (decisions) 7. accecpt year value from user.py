def year() :
    a = int(input("Enter a year : "))

    if a%4 == 0 and a%400 == 0:
        print("Given year is a leap year")
    else:
        print("Given year is not a leap year")

year()
    
