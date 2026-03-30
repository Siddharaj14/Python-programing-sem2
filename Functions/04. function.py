def sum_avg() :
    s = 0
    for x in range(6):
        m = int(input("Enter marks : "))
        s = s + m
    return (s,s/6)
print(sum_avg())
