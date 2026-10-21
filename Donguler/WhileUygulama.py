import random


sayilar = [1,3,5,7,9,12,19,21]
#1: sayilar listesini while ile ekrana yazdırın.]
# i=0
# while sayilar:
#   print(sayilar)
#   break;
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
# tek sayıları ekrana yazdırın.
# baslangic = int(input("Başlangıç sayısını giriniz: "))
# bitis = int(input("Bitiş sayısını giriniz: "))

# while baslangic <= bitis:
#     if baslangic % 2 != 0:
#         print(baslangic)
#     baslangic += 1

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
# x=100
# while x>=0:
#    print(x)
#    x -=1
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
# yazdırın.

# sayilar = []
# i = 0
# while i < 5:
# 	sayilar.append(int(input(f"{i + 1}. sayıyı giriniz: ")))
# 	i += 1

# sayilar.sort()
# print(sayilar)

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayın
# ** ürün sayısını kullanıcıya sorun.
# ** dictionary listesi yapısı (name, price) şeklinde olsun.
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
urunler = []
fiyatlar= []

adet=int(input("Kaç ürün eklemek istiyorsunuz:"))
i=0
while i<adet:
    urun=input(f"Lütfen ekleme istediğiniz {i+1}. Ürünü giriniz:")
    urunler.append(urun)
    rastgele_fiyat=random.randint(20,300)
    fiyatlar.append(rastgele_fiyat)
    i+=1
    print(urunler)
    print("\n--- Ürün ve Fiyat Listesi ---")

i = 0
while i < len(urunler):
    print(f"Ürün: {urunler[i]:<15} | Fiyat: {fiyatlar[i]} TL")
    i += 1