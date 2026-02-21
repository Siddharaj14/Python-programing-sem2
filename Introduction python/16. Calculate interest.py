def interest() :
    P = int(input("Enter principle : "))
    R = int(input("Enter rate : "))
    T = int(input("Enter time(in year) : "))

    I = P*R*T/100

    print("Interest is :",I)

interest()
