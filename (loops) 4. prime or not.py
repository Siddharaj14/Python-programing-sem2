def loop4() :
    n = int(input("Enter a number : "))

    for d in range(3,n):
        if n%d == 0:
            print("not prime")
        else:
            print("prime")
    print("is a prime number",n)

loop4()
