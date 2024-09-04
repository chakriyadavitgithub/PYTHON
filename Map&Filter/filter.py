#without filter
product_prices=[1000,2000,300,200,10,40,500]
#display all product prices below 1000
new_prices=[]
for price in product_prices:
    if price <=1000:
        new_prices.append(price)
        print(new_prices)