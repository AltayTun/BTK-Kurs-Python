sayilar=[]
for x in range(10):
    sayilar.append(x)
print(sayilar)

print("*"*5)

sayilar=[x for x in range(10)]
print(sayilar)

print("*"*5)

for x in range(10):
    print(x**2)

print("*"*5)

sayilar=[x**2 for x in range(10)]
print(sayilar)

print("*"*5)


sayilar=[x*x for x in range(10) if x%3==0]
print(sayilar)

print("*"*5)


# Bir üste yaptığımız uygulamanın açılmış hali
sayilar=[]
for x in range(10):
    if x%3==0:
        sayilar.append(x*x)
        print(sayilar) #Eğer bunu if'in dışına alırsak alt alta piramit şeklinde yazmaz tek satırda işi bitirir

print("*"*5)

myString="Hello"
liste=[]
for letter in myString:
    liste.append(letter)
print(liste)


print("*"*5)

liste=[letter for letter in myString]
print(liste)

print("*"*5)

yil=[1983,1999,2008,1956,1986]
yas=[2026-yi for yi in yil]
print(yas)

print("*"*5)

bilgi=[x if x%2==0 else f"{x}:TEK" for x in range(1,10)]
print(bilgi)

print("*"*5)


bilgi=[]

for x in range(3):
    for y in range(3):
        bilgi.append((x,y))
        print((x,y),end="")
    print()
    
print("*"*5)

sayilar=[(x,y) for x in range(3) for y in range(3)]
print(sayilar)

print("*"*5)
#alta geçmesi için
sayilar=[(x,y) for x in range(3) for y in range(3)]
for i in range(len(sayilar)):
    print(sayilar[i],end="")
    if(i+1)%3==0:
        print()