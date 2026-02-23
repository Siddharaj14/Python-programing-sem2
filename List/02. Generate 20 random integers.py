import random
def list2() :
    otp = [random.randrange(100000,999999) for x in range(20)]
    print(otp)
    n = int(input("Enter a number : "))
    if n in otp:
        for i,v in enumerate(otp):
            if v == n:
                print(i)
    else:
        print(n,"Not found")

list2()
