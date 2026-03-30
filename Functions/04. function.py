def sum_avg() :
    s = 0
    for x in range(5):
        m = int(input("Enter marks : "))
        s = s + m
    return (s,s/5)
print(sum_avg())
