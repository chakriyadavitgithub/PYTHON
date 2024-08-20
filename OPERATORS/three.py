##python sequence?
# strng,list,tuple,dict,range,bytes,bytearray,forzenset
ename="chakri"
l=[10,20,30]
t=(10,20,30,40)
s={10,20,30}
d={'id':101,'name':'priya','avail':True}
r=range(10,20,30)
b=bytes(l)
ba=bytearray(l)
fs=frozenset(s)
print(ename)
print(l)
print(t)
print(s)
print(d)
print(r)
print(b)  #b'\n\x14\x1e'
print(ba) #bytearray(b'\n\x14\x1e')
print(fs)