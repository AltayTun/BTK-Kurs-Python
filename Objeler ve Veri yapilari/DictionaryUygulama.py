
ogrenciler ={

"120":
{
    "ad":"Ali",
    "soyad":"Yılmaz",
    "telefon":"532 000 00 01"
},
"125":
{
"ad":"Can",
"soyad":"Korkmaz",
"telefon":"532 000 00 01"
},
"128":
{
    "ad":"Volkan",
    "soyad":"Yükselen",
    "telefon":"532 000 00 03"
},

}
'''
1- Bilgileri verilen öğrencileri kulanıcdan aldığınız
bilgilerle dictionary içinde saklayınız.

2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''

#1
print("Öğrenci kayıt Sistemi")
print("---------------------")
numara=input("Lütfen öğrenci numarasını giriniz: ")
ad=input("Lütfen öğrenci adı giriniz: ")
soyad=input("Lütfen öğrenci soyadı giriniz: ")
telefon=input("Lütfen öğrenci telefon no giriniz: ")
ogrenciler={
numara:
{
    "ad":ad,
    "soyad":soyad,
    "telefon":telefon
}
}
print(ogrenciler)
#2
numara=input("Öğrenci No:")
ogrenci=ogrenciler[numara]
print(ogrenci)
