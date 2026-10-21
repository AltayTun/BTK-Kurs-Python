x,y,z=2,5,107
sayilar=1,5,7,10,6

# 1- Kullanıcdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
sayi1=int(input("1.Sayıyı giriniz:"))
sayi2=int(input("2.Sayıyı giriniz:"))
sonuc=sayi1*sayi2-x+y+z
print(sonuc)
# 2- y'nin x'e kalansız bölümünü hesaplayınız.
deger=y//x
print(deger)
# 3- (x,y,z) toplamının mod 3'ü nedir ?
deger=x+y+z%3
print(deger)
# 4- y'nin x. kuvvetini hesaplayınız.
deger=y**x
print(deger)
# 5- x, *y,z=sayilar işlemine göre z'nin küpü kaçtır ?
sayilar=1,5,7,10,6
x , *y ,z=sayilar
print(sayilar)
deger=z**3
print(deger)
# 6- x, *y,z=sayilar işlemine göre y'nin değerleri toplamı kaçtır
x,*y,z=sayilar
deger=y[0]+y[1]+y[2]
print(deger)