# s={}
# print(type(s))#class dict
# s1={10,20,30,20,10,40,50,60}
# print(s1)# output:{50, 20, 40, 10, 60, 30} order guranate is not required.

#eids={101,202,101,405,201,101,"chakri","rahul",202}
#print(eids) #o/p:{'rahul', 101, 405, 201, 202, 'chakri'}

# s1={10,20,30}
# s2={40,50,60}
# s1.update(s2)
# print(s1)#o/p:{50, 20, 40, 10, 60, 30}

s1={10,20,30}
s2={40,50,60}
s1.add(80)
s2.add(100)
print(s1)         #o/p: {80, 10, 20, 30}
print(s2)        # o/p:{40, 100, 50, 60}
