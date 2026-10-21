# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#    lise ya da üniversite olmalıdır.
isim=input("Adınızı giriniz:")
yas=int(input("Yaşınızı giriniz:"))
egitim=input("Eğitim durumunuzu giriniz:")

if yas>=18:
    if egitim=="Lise,Üniversite":
        print("Ehliyeti Alma koşullarını başarıyla sağladınız.Tebrikler")
    else:
        print("Egitim düzeyiniz ehliyet alma koşulu için yeterli değil")
else:
    print("Yaşınız ehliyet alma düzeyinde değil ")
        
    
# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
# 0 -24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => A
# 85-100 => 5

yazili1=int(input("1. Yazılı giriniz:"))
yazili2=int(input("2. Yazılı giriniz:"))
sözlü=int(input("Sözlü giriniz:"))

ortalama=(yazili1+yazili2+sözlü)/3
if ortalama>0 and ortalama<=24:
    {
    print(f'Ortalamanız:{ortalama}\nNot bilgisi = 0')
    }
elif ortalama>=25 and ortalama<=44:
     {
     print(f'Ortalamanız:{ortalama}\nNot bilgisi = 1')
     }
elif ortalama>=45 and ortalama<=54:
          {
     print(f'Ortalamanız:{ortalama}\nNot bilgisi = 2')
          }
elif ortalama>=55 and ortalama<=69:
                  {
                    print(f'Ortalamanız:{ortalama}\nNot bilgisi = 3')
                    }
elif ortalama>=70 and ortalama<=84:
                              {
                              print(f'Ortalamanız:{ortalama}\nNot bilgisi = 4')
                              }
elif ortalama>=85 and ortalama<=100:
                                        {
                                        print(f'Ortalamanız:{ortalama}\nNot bilgisi = 5')
                                        }
     
        
# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
# göre hesaplayınız.
# 1. Bakım => 1. yıl
# 2. Bakım => 2. yıl
# 3. Bakım => 3. yıl
# ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
# ***datetime modülünü kullanmanız gerekiyor.

import datetime
tarih_str = input("Trafiğe çıkış tarihini giriniz (GG/AA/YYYY): ")

gun, ay, yil = map(int, tarih_str.split("/"))
trafige_cikis = datetime.date(yil, ay, gun)
bugun = datetime.date.today()
fark = bugun - trafige_cikis
gecen_gun = fark.days
if gecen_gun <= 365:
    print(f"Araç {gecen_gun} gündür trafikte: 1. Bakım aralığında.")
elif gecen_gun <= 365 * 2:
    print(f"Araç {gecen_gun} gündür trafikte: 2. Bakım aralığında.")
elif gecen_gun <= 365 * 3:
    print(f"Araç {gecen_gun} gündür trafikte: 3. Bakım aralığında.")
else:
    print(f"Araç {gecen_gun} gündür trafikte: 3. Bakım süresi de geçmiş veya daha ileri bir bakım dönemi.")