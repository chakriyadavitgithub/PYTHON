numbers=[0,1,2,3,4,5,6,7,8,99,45,66,67,88,33,22,44]
evens=0
odds=0
for number in numbers:
    if number %2==0:
        evens=evens+1
    else:
        odds=odds+1
print("No of even no:",evens)
print("No of odd no:",odds)

    