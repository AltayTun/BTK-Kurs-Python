isim="Ahmet"
soyadim="Yılmaz"
yas=30
selamlama ="Benim adım " + isim + " \nSoyadım " + soyadim + " \nYaşım " + str(yas)
uzunluk=len(selamlama)

print(selamlama)     
print(selamlama[0])         #sadece 0. karakteri almak için 0 kullanılır.
print(selamlama[3])         #sadece 3. karakteri almak için 3 kullanılır.
print(len(selamlama))       #uzunluğu almak için len() fonksiyonu kullanılır.
print(selamlama[uzunluk-1]) #son karakteri almak için uzunluk-1 kullanılır.
print(selamlama[-1])        #son karakteri almak için -1 kullanılır.
print(selamlama[2:5])       #2 den başlayıp 5 e kadar olan karakterleri alır. 5 dahil değil.
print(selamlama[3:])        #3 den başlayıp sonuna kadar olan karakterleri alır.
print(selamlama[:5])        #0 dan başlayıp 5 e kadar olan karakterleri alır. 5 dahil değil.
print(selamlama[2:40:2])    #2 şer 2 şer atlayarak karakterleri alır.



