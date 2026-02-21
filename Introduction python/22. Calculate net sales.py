def net_sales() :
    gross_sales = int(input("Enter gross sales : "))
    discount = 10/100*gross_sales

    net_sales = gross_sales - discount

    print("Net sales is :",net_sales)

net_sales()
