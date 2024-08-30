#pop remove specified key & associate values
# emp={'eid':101,'ename':'chakri','esal':40000}
# emp.pop('eid')
# print(emp)#{'ename': 'chakri', 'esal': 40000}


emp={'ename': 'chakri', 'esal': 40000}
emp.popitem()
#clear
emp.clear()#{}
print(emp)#{'ename': 'chakri'}