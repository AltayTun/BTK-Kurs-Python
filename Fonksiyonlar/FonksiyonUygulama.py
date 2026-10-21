# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazı

def gonderilen_kelime(kelime,adet):
    for i in range(adet):
        print(kelime)
gonderilen_kelime("Emre",5)
        
# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonks 
def sinirsiz_giris(*giris):
    for i in giris:
        print(i,end=" ")
    print()

sinirsiz_giris(10,20,30,40)
print("-"*50)

#diğer yol
def listeye_cevir(*params):
    liste=[]

    for param in params:
        liste.append(param)
    return liste
print(listeye_cevir(10,20,30,"Merhaba"),end=" ")

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
def asal_sayi(sayi1,sayi2):
    for i in range(sayi1+1,sayi2):
        if i%2>0:
            print(i,end=(" "))
asal_sayi(10,30)

# diğer yöntem 
sayi1=int(input("1.Sayıyı giriniz:"))
sayi2=int(input("2.Sayıyı giriniz:"))
def asal_sayilari_bul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi>1:
            for i in range(2,sayi):
                if sayi%i==0:
                    break
            else:
                print(sayi)
asal_sayilari_bul(sayi1,sayi2)


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür
def tam_bolunen(sayi):
    bolenler=[]
    for i in range(1,sayi+1):
        if sayi%i==0:
            bolenler.append(i)
    return bolenler
print(tam_bolunen(15))            