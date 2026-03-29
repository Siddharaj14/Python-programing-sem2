def string1() :
    str1 = input("Enter a string : ")
    count = 0
    vowels = "aeiouAEIOU"

    for char in str1:
        if char in vowels:
            count += 1
    print("Number of vowels in string :",count)

string1()
