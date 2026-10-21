# 1- "Bmw,Mercedesi,Opel,Mazda"elemanlarına sahip bir liste oluşturunuuz"
marka=["Bmw", "Mercedes","Opel","Mazda"]
print(marka)
# 2- "Liste kaç Elamnlıdır?"
print(len(marka))
# 3- "Listenin ilk ve son elemanı nedir"
print(marka[0])
print(marka[3])
# 4- "Mazda değerini Toyota ile değiştirin"
marka.insert(4,"Toyota")
print(marka)
# 5- "Mercedes listenin bir elemanı mıdır?"
bilgi="Mercedes" in marka
print(bilgi)
# 6- "Listenin -2 indeksindeki değer nedir?"
print(marka[-2])
# 7- "Listenin ilk 3 elemanını alın."
marka.pop(4)
print(marka)
# 8- "Listenin son 2 elemanı yerine "Toyota" ve "Renault"değerlerini ekleyin."
marka.insert(3,"Toyota")
marka.insert(2,"Renault")
print(marka)
# 9- "Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
marka.insert(4,"Audi")
marka.insert(5,"Nissan")
print(marka)
# 10- "Listenin son elemanını silin."
marka.pop(5)
print(marka)
# 11- "Liste elemanalrını tersten yazdırınız",
print(marka[::-1])
# 12- "Aşağıdaki verileri bir liste içinde saklayınız."
# studentA: Yiğit Bilgi 2010, (70,60,70)
# studentA: Sena Turan 1999, (80,80,70)
# studentA: Ahmet Turan 1999, (80,70,90)
ogrenciBilgileri=["Yigit Bilgi0,2010,70,60,70","Sena Turan,1999,80,80,70","Ahmet Turan,1999,80,70,90"]
# 13- "Liste elemanlarını ekrana yazdırınız"
print(ogrenciBilgileri)
