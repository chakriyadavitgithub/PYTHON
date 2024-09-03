#map=function & sequence
# def add(mark):
#     return mark+1
# marks=[25,40,50]
# object=map(add,marks)
# print(object)
# print(type(object))
# print(list(object))


#by using lambda
print(list(map(lambda m:m+1,[23,56,34])))
marks=[24,39,40]
object=map(lambda mark:mark+1,marks)
print(list(object))
