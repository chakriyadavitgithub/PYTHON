# with lambada
numbers=[10,20,30,40]

map_obj=map(lambda num : num+1,numbers)
new_numbers=list(map_obj)
print(numbers)
print(new_numbers)


#output:
# [10, 20, 30, 40]
# [11, 21, 31, 41]