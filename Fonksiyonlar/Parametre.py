def changeName(n):
    n="ada"
name="Yiğit"
changeName(name)
print(name)

def change(n):
    n[0]="İstanbul"
sehirler=["Ankara","İzmir"]

change(sehirler)
print(sehirler)


def chang(n):
    n[0]="İstanbul"
sehirler=["Ankara","İzmir"]
n=sehirler[:] # slicing
n[0]="İstanbul"
print(sehirler)
print(n)

def change(n):
    n[0]="İstanbul"
sehirler=["Ankara","İzmir"]

change(sehirler[:])
print(sehirler)

# def add(a,b):
#     return sum(a,b,c=0,d=0)

# print(add(10,20))
# print(add(10,20,30))

def add(*params):
    print(params)
    return sum((params))
print(add(10,20,50))
print(add(10,20,30))
print(add(10,20,30,40,50,60))

# def add(*params):
#     sum=0
#     for n in params:
#         sum=sum+n
#     return sum

# print(add(10,20,50))
# print(add(10,20,30))
# print(add(10,20,30,40,50,60))



def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name="Çınar", age=2,city="İstanbul")
displayUser(name="Ada", age=12,city="Kocaeli",phone="12345")
displayUser(name="Yiğit", age=14,city="Ankara",phone="12345",email="yigit@gmail.com")

def myfunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myfunc(10,20,30,40,50,key1="value 1",key2="value 2",key3="value 3")