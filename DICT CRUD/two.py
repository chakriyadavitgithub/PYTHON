emp={'eid':101,'ename':'chakri','esal':40000}
##by using the for lopp
for key in emp.keys():
    print(key)
    print("*******")

    for value in emp.values():
        print(value)
        
        for item in emp.items():
            print(item)
