#duplicate keys are not allowed.
# emp={'eid':10,'eid':20,'eid':30,}
# print(emp)

#print all dict values?
emp={'eid':101,'ename':'Chakri','esal':3000,'avail':True}
print(emp['eid'])
print(emp['ename'])
print(emp['esal'])
print(emp['avail'])

#print all dict values by using get?
emp={'eid':101,'ename':'Chakri','esal':3000,'avail':True}
print(emp.get('eid'))
print(emp.get('ename'))
print(emp.get('esal'))
print(emp.get('avail'))

