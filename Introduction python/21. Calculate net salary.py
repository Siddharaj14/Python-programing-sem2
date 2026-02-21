def net_salary() :
    gross_salary = int(input("Enter gross salary : "))
    allowance = 10/100*gross_salary
    deduction = 3/100*gross_salary

    net_salary = gross_salary + allowance - deduction

    print("Net_salary is :",net_salary)

net_salary()
