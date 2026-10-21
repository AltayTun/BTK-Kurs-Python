# 1- Girilen 2 sayıdan hangisi büyüktür ?
sayi1=input("1.Sayıyı giriniz:")
sayi2=input("2.Sayıyı giriniz:")
sonuc1=sayi1>sayi2
print("İlk sayı:",{sayi1},"İkinci sayı:",{sayi2}, "den büyüktür:",sonuc1)
sonuc2=sayi2>sayi1
print("İkinci sayı:",{sayi2},"Birinci sayı:",{sayi1}, "den büyüktür:",sonuc2)

# 2- Kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
vize1=float(input("1.Vize notunuzu giriniz:"))
vize2=float(input("2.Vize notunuzu giriniz:"))
final=float(input("Final notunuzu giriniz:"))
ortalama=((vize1+vize2)*0.60+final*0.40)/2
ort=ortalama>=50
print(ort,"Geçtiniz")
ort1=ortalama<50
print(ort1,"kaldınız")

# 3- Girilen bir sayının tekmi çift mi olduğunu yazdırın
sayi=int(input("Bir sayı giriniz:"))
sayi1=sayi%2==0
print("Çift sayıdır:",{sayi1})

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın
sayi=int(input("Bir sayı giriniz:"))
sayi1=sayi>=0
print("Pozitif sayıdır:",{sayi1})

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz..
# (email: email@sadikturan.com parola:abc123)
etmail="email@sadikturan.com"
parola="abc123"
mail=input("email:")
sifre=input("şifre:")

kontrol1=etmail==mail
print(kontrol1)
kontrol2=parola==sifre
print(kontrol2)


