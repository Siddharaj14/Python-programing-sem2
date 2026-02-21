def triangle() :
    a = int(input("Enter angle 1 of the triangle : "))
    b = int(input("Enter angle 2 of the triangle : "))
    c = int(input("Enter angle 3 of the triangle : "))

    sum = a+b+c

    if sum == 180:
        print("Given triangle is valid as sum of angles is 180")
    else:
        print("Given triangle is not valid as sum of angles is not 180")

triangle()
