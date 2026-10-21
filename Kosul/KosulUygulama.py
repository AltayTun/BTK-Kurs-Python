#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input('sayı: '))
if sayi>0 and sayi<100:
    print(f"Sayınız :{sayi} \n0 ile 100 arasında 0<{sayi}<100")
else:
    print(f"Sayınız :{sayi} \n0 ile 100 arasında değil ")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
sayi = int(input('sayı: '))
if sayi%2==0:
    if sayi>0:
        print("girilen sayı pozitif çift sayı")
    else:
        print("girilen sayı pozitif ancak tek sayı")
else:
    print("girilen sayı pozitif çift sayı değildir.")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'email@sadikturan.com'
password = 'abc123'

mail=input("Lütfen e-mail adresinizi giriniz:")
sifre=input("Lütfen şifrenizi giriniz:")

if email==mail:
    if password==sifre:
       print("Girdiğiniz bilgiler doğru")
    else:
       print("Şifreniz yanlış")
else:
       print("Email adresiniz yanlış")
   
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a>b and a>c:
    print(f"En büyük sayı a dir \n{a}")
elif b>a and b>c:
    print(f"En büyük sayı b dir \n{b}")
else:
    print(f"En büyük sayı c dir \n{c}")



# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
# b-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1 = float(input('vize 1: '))
vize2 = float(input('vize 2: '))
final = float(input('final :'))
ortalama = ((((vize1+vize2))/22))**0.6+ (final * 0.4)

# # İstenen
if ortalama>=50:
    print(f"Geçtiniz ({ortalama})")
else:
    print(f"Kaldınız ({ortalama})")
# #a
if ortalama>=50 and final>=50:
    print(f"Geçtiniz ({ortalama})")
else:
    print(f"Kaldınız ({ortalama})")
#b
if final>=70 :
    print(f"Geçtiniz ({final})")
else:
   if ortalama >=50:
       print(f"Geçtiniz ({ortalama})")
   else:
       print(f"Kaldınız ({ortalama})")
       


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# Formül: (Kilo / boy uzunluğunun karesi)
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
# 0-18.4 => Zayıf
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla kilolu
# 30.0-34.9 => Şişman (Obez)
name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))
index=(kg) / (hg ** 2)

if index>0 and index<=18.4:
    print(f"İndeksiniz zayıftır \n İndeks oranınız:{index}")
elif index>=18.5 and index<=29.9:
    print(f"İndeksiniz normaldir \n İndeks oranınız:{index}")
elif index>=30.0 and index<=34.9:
    print(f"İndeksiniz fazla kiloludur \n İndeks oranınız:{index}")
elif index>=35.0:
    print(f"İndeksiniz şişmandır (obez) \n İndeks oranınız:{index}")
else:
    print("Geçersiz kilo veya boy bilgisi girdiniz.")