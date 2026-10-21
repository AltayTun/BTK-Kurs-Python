'''

1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
(hak = 5)
** "random modülü" için "python random" şeklinde arama yapın.
** 100 üzerinden puanlama yapın. Her soru 20 puan.
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''
import random
rastgele = random.randint(1, 100)

print("<----------SAYI TAHMİN OYUNU---------->")

can = int(input("Sayıyı tahmin etmek için kaç hakkınız olsun: "))

if can <= 0:
    print("Geçersiz can girdiniz, sistem otomatik olarak 5 hak verdi.")
    can = 5

toplam_hak = can  
puan_adimi = 100 / toplam_hak

tahmin = int(input("Sayı tahmin edildi, seçtiğim sayıyı bul: "))

while tahmin != rastgele:
    can -= 1 

    if can == 0:
        print(f"\nKAYBETTİNİZ! Canınız bitti. Tutulan sayı: {rastgele}")
        break
    if tahmin > rastgele:
        print("AŞAĞI")
    elif tahmin < rastgele:
        print("YUKARI")
    tahmin = int(input(f"YANLIŞ! Kalan can: {can} | Yeni tahmin gir: "))

if can > 0:
    kazanilan_puan = int(can * puan_adimi)
    print(f"\nTEBRİKLER !!! Seçtiğim sayıyı buldun: {rastgele}")
    print(f"PUANINIZ: {kazanilan_puan}")