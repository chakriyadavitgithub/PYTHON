 #with filter & with out lambda
product_prices=[1000,200,500,300,2000,3000,20]
def filterdata(price):
    return price<1000
new_prices=list(filter(filterdata,product_prices))
print(product_prices)
print(new_prices)