#empty dict object
# emp={}
# emp['name']='chakri'
# emp['name']='yadav'
# print(emp)#{'name': 'yadav'}


# emp={'name':'chakri'}
# emp.update('eid',101)
# print(emp)#type error will be occur

#update dict 
emp={'name':'chakri'}
emp.update({'eid':101})
print(emp)#{'name': 'chakri', 'eid': 101}