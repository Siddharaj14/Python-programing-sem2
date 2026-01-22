def straight() :
    x1 = int(input("Enter x1 : "))
    y1 = int(input("Enter y1 : "))
    x2 = int(input("Enter x2 : "))
    y2 = int(input("Enter y2 : "))
    x3 = int(input("Enter x3 : "))
    y3 = int(input("Enter y3 : "))

    area = 1/2*(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1-y2))

    if area == 0:
        print("Points lies on the straight line")
    else:
        print("Points does not line on the straight line")

straight()
