# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# sayi=int(input("Bir sayı giriniz:"))
# sayi>0 and sayi<100
# sayi==True
# print("İçerisinde")
# sayi==False
# print("İçerisinde değil")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# sayi=int(input("Bir sayı giriniz:"))
# sayi>0 and sayi%=2==0
# print(sayi)
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
# mail="email@emrealtun"
# sifre="123456"

# kulmail=input("Email:")
# kulsife=input("Sifre:")

# a=kulmail==mail and kulsife==sifre
# print(a)

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# sayi1=input("Birinci sayı giriniz:")
# sayi2=input("İkinci sayı giriniz:")
# sayi3=input("Üçüncü sayı giriniz:")
# sonuc=sayi1>sayi2 and sayi1>sayi3
# print("sayi1 en büyük sayıdır:",(sonuc))
# sonuc=sayi2>sayi1 and sayi2>sayi3
# print("sayi2 en büyük sayıdır:",(sonuc))
# sonuc=sayi3>sayi2 and sayi3>sayi1
# print("sayi3 en büyük sayıdır:",(sonuc))

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# vize1=int(input("1.Vize notunuzu giriniz:"))
# vize2=int(input("2.Vize notunuzu giriniz:"))
# final=int(input("Final notunuzu giriniz:"))

# ortalama=((vize1+vize2)*0.60+final*0.40)/2

# # Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# sonuc=ortalama>=50 and ortalama<50 
# print("Öğrencinin Ortalaması:",ortalama,"Kalma durumu:",sonuc)

# # a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
# sonuc=ortalama>=50 and final>50
# print("Öğrencinin Ortalaması:",ortalama,"Kalma durumu",sonuc)

# # b-) Finalden 70 alındığında ortalamanın önemi olmasın.
# sonuc=final>=70 or ortalama>=50
# print("Final sonucu:",final,"Geçme durumu:",sonuc)

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# Formül: (Kilo boy uzunluğunun karesi)
ad=input("Adınızı Giriniz:")
kilo=float(input("Kilonuzu giriniz:"))
boy=float(input("Boyunuzu giriniz:"))

indeks=kilo/boy**2
print(indeks)
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
# 0-18.4 => Zayıf
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla kilolu
# 30.0-34.9 => Şişman (Obez)
durum=indeks>=0 and indeks<=18.4
durum=="Zayıf"
print("Vücut Kütle İndeksiniz:",indeks,"Girilen grup:Zayıf",durum)
durum=indeks>=18.5 and indeks<=24.9
durum=="Normal"
print("Vücut Kütle İndeksiniz:",indeks,"Girilen grup:Normal",durum)
durum=indeks>=25.0 and indeks<=29.9
durum=="Fazla kilolu"
print("Vücut Kütle İndeksiniz:",indeks,"Girilen grup:Fazla Kilolu",durum)
durum=indeks>=30.0 and indeks<=34.9
durum=="Şişman(Obez)"
print("Vücut Kütle İndeksiniz:",indeks,"Girilen grup:Şişman(obez)",durum)