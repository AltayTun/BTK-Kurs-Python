names=["Ali","Yağmur","Hakan","Deniz"]
years=[1998,2000,1998,1987]

#  1- "Cenk" İsmini listenin sonuna ekleyiniz.
a=names.append("Cenk")
print(a)
#  2- "Sena" Değerini listenin başına ekleyiniz.
a=names.insert(1,"Sena")
print(a)
#  4- "Deniz"isminin indeksi nedir.
print(names.count("Deniz"))
#  4- "Deniz" İsmini listeden siliniz
names.remove("Deniz")
print(names)
#  5- "Ali" Listenin bir elemanımıdır.
result ="Ali" in names
print(result)
#  6- Liste elemanlarını ters çeviriniz
names.reverse()
print(names)
#  7- liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)
#  8- years listesini rakamsal büyüklüğe göre sıralayınız
years.sort()
print(years)
#  9- str="Cehvrolet,Dacia" karakter dizisini listeye çeviriniz
str=["Chevrolet","Dacia"]
# 10- years dizisinin en büyük ve en küçük elemanı nedir?
b=max(years)
print(b)
b=min(years)
print(b)
# 11- years dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))
# 12- years dizisinin tüm elemanlarını siliniz.
print(years.clear)
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
marka1=input("1.Markaya Giriniz:")
marka2=input("2.Markaya Giriniz:")
marka3=input("3.Markaya Giriniz:")

markalar =[marka1,marka2,marka3]
print("Listeniz Hazır:",markalar)
