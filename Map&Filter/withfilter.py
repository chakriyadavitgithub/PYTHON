#with filter & with lambda function
product_prices=[1000,200,500,300,2000,3000,20]
new_prices=list(filter(lambda price:price<1000,product_prices))
print(product_prices)
print(new_prices)

