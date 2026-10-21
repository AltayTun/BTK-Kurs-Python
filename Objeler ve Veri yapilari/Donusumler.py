
# x =  input('1 Sayıyı giriniz: ')
# y =  input('2 Sayıyı giriniz: ')

# print(type(x))
# print(type(y))
# toplam=int(x) + int(y)  
# print("Toplam:", toplam)

x=5           #int
y=2.5         #float  
name="Ali"    #string
isOnline=True #boolean

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

#Type Conversion

#int to float
x=float(x)
print("x:", x)
print("x type:", type(x))

#float to int
y=int(y)
print("y:", y)
print("y type:", type(y))

result=str(x)+str(y)
print("result:", result)
print("result type:", type(result))

#bool to string

isOnline=str(isOnline)
print("isOnline:", isOnline)
print("isOnline type:", type(isOnline))

#bool to int

isOnline=int(isOnline)
print("isOnline:", isOnline)
print("isOnline type:", type(isOnline))