def area() :
    l = int(input("Enter length of rectangle : "))
    b = int(input("Enter breadth of rectangle : "))

    area = l*b
    perimeter = 2*(l+b)

    if area > perimeter:
        print("Area of rectangle is greater than it's perimeter")
    elif perimeter > area:
        print("Perimeter of rectangle is greater than it's area")
    else:
        print("Area is equal to Perimeter")

area()

    
