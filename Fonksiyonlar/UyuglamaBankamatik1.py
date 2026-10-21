# Bankamatik Uygulaması

Emre_Hesap = {
    "ad": "Emre Çağatay Altun",
    "hesapNo": "12345678999",
    "bakiye": 3000,
    "ekHesap": 2000,
    "sifre": "0123",
    "kod": "4321",
}
Ali_Hesap = {
    "ad": "Ali Yılmaz",
    "hesapNo": "12345678888",
    "bakiye": 5000,
    "ekHesap": 3000,
    "sifre": "3210",
    "kod": "1234",
}


def atm_menu_ekrani(aktif_hesap):
  print("=" * 50)
  print(f"|{'BANKA ATM - ANA MENÜ':^49}|")
  print("=" * 50)
  print(f"| {'Hesap Sahibi':<20} : {aktif_hesap['ad']:<24} |")
  print(f"| {'Hesap Bakiyesi':<20} : {aktif_hesap['bakiye']:<24} |")
  print(f"| {'Ek Hesap Bakiyesi':<20} : {aktif_hesap['ekHesap']:<24} |")
  print(f"| {'Hesap Numarasi':<20} : {aktif_hesap['hesapNo']:<24} |")
  print("=" * 50)
  print(f"|{'İŞLEMLER:':<48} |")
  print(f"|{'[1] Para Transferi':<48} |")
  print(f"|{'[2] Para Yatırma':<48} |")
  print(f"|{'[3] Para Çekme':<48} |")
  print(f"|{'[4] Çıkış':<48} |")
  print("=" * 50)
  kullanici_islem = input("Lütfen yapmak istediğiniz işlemi tuşlayınız: ")
  return kullanici_islem


def atm_islem(aktif_hesap):
  secim = atm_menu_ekrani(aktif_hesap)

  if secim == "1":
    iban_giris = input("Lütfen alıcı IBAN'ını giriniz: ")
    yollanicak_tutar = float(input("Göndereceğiniz tutarı giriniz: "))

    if aktif_hesap["bakiye"] < yollanicak_tutar:
      cevap = input("Hesap bakiyeniz yetersiz! Ek hesaptan ekleme yapalım mı? (EVET / HAYIR): ").upper()
      if cevap == "EVET":
        toplam_bakiye = aktif_hesap["bakiye"] + aktif_hesap["ekHesap"]
        if toplam_bakiye < yollanicak_tutar:
          print("Bakiyeniz ve ek hesabınız gönderilecek tutarı karşılamıyor.")
        else:
          print("Ek hesaptan kullanılarak para gönderiliyor")
          kalan_tutar=yollanicak_tutar-aktif_hesap["bakiye"]
          aktif_hesap["bakiye"]=0
          aktif_hesap["ekHesap"]-=kalan_tutar
          baska_islem=input("Söylediğiniz tutar gönderildi başka işlem yapmak istiyormusunuz (EVET / HAYIR):")
          if baska_islem=="EVET":
            atm_islem(aktif_hesap)
          elif baska_islem=="HAYIR":
            print("İyi günler")
      elif cevap == "HAYIR":
        print("İşlem iptal edildi.")
    else:
      print("Para transferi gerçekleştiriliyor...")

  elif secim == "2":
    yatirilacak_tutar=int(input("Lütfen yatırmak istediğniiz tutarı giriniz: "))
    sayac=3
    while sayac>0:
      if yatirilacak_tutar>0 and yatirilacak_tutar<10000:
        print("Yatırma işlemi tamamlandı.")
        aktif_hesap["bakiye"]+=yatirilacak_tutar
        print(f"Güncel Bakiye: {aktif_hesap['bakiye']:,}TL")
        baska_islem=input("Başka işlem yapmak istiyormusunuz (EVET / HAYIR) :").upper()
        if baska_islem=="EVET":
          atm_islem(aktif_hesap)
        elif baska_islem=="HAYIR":
          print("İyi günler")
        break
      elif yatirilacak_tutar<0 or yatirilacak_tutar>10000:
        sayac-=1
        yatirilacak_tutar=int(input(f"Kalan hak {sayac} || Limitten fazla para yatırılamaz lütfen tekrar deneyin:"))
        if sayac==0:
          print("Hakkınız bitti ana menüye yönlendiriliyorsunuz...")
          atm_islem(aktif_hesap)
        break
      else:
        sayac-=1
        yatirilacak_tutar=int(input(f"Kalan hakkınız: {sayac} || Eksik ya da hatalı tuşladınız lütfen tekrar deneyin"))
        if sayac==0:
          print("Hakkınız bitti menüye yönlendiriliyorsunuz...")
          atm_islem(aktif_hesap)
        break
    

  elif secim == "3":
    para_cekme = int(input("Lütfen çekeceğiniz tutarı giriniz: "))
    toplam_bakiye = aktif_hesap["bakiye"] + aktif_hesap["ekHesap"]

    if aktif_hesap["bakiye"] < para_cekme:
      cevap = input( "Hesap bakiyeniz yetersiz! Ek hesaptan ekleme yapalım mı? (EVET / HAYIR): ").upper()
      if cevap == "EVET":
        if toplam_bakiye < para_cekme:
          print("Bakiyeniz ve ek hesabınız tutarı karşılamıyor.")
        else:
          print("Ek hesaptan kullanılarak para hazırlanıyor...")
          kalan_tutar = para_cekme - aktif_hesap["bakiye"]
          aktif_hesap["bakiye"] = 0
          aktif_hesap["ekHesap"] -= kalan_tutar
          print(f"Güncel Ana Bakiye: {aktif_hesap['bakiye']} TL")
          print(f"Güncel Ek Hesap: {aktif_hesap['ekHesap']} TL")

      elif cevap == "HAYIR":
        sayac = 3
        while sayac > 0:
          if para_cekme > aktif_hesap["bakiye"]:
            sayac -= 1
            if sayac == 0:
              print("Çok fazla hatalı tutar girişi! Kartınız iade ediliyor.")
            break
          elif toplam_bakiye >= para_cekme:
            print("Paranız hazırlanıyor...")
            aktif_hesap["bakiye"] -= para_cekme
            print(f"Hesapta kalan tutar: {aktif_hesap['bakiye']} TL")
            islem = input("Başka işlem yapmak istiyor musunuz? (EVET / HAYIR): ").upper()
            if islem == "EVET":
              atm_islem(aktif_hesap)
            break
    else:
      aktif_hesap["bakiye"] -= para_cekme
      print("Paranız hazırlanıyor... İyi günlerde harcayın.")
      print(f"Hesapta kalan tutar: {aktif_hesap['bakiye']} TL")
      islem = input("Başka işlem yapmak istiyor musunuz? (EVET / HAYIR): ").upper()
      if islem == "EVET":
        atm_islem(aktif_hesap)

  elif secim == "4":
    cikis = input("Çıkmak istediğinizden emin misiniz? (EVET / HAYIR): ").upper()
    if cikis == "EVET":
      print("Kart iade ediliyor... İyi günler dileriz.")
    elif cikis == "HAYIR":
      atm_islem(aktif_hesap)


def atm_giris_sistemi():
  print("=" * 50)
  baslik = "ATM'ye HOŞGELDİNİZ"
  print(f"{baslik:^50}")
  print("=" * 50)

  giris_sekli = input(
      "Giriş yapmak istediğiniz şekli seçin (QR / Kart): "
  ).upper()
  sayac = 3
  while sayac > 0:
    if giris_sekli == "KART":
      kullanici_sifre = input("Lütfen kartınızın şifresini giriniz: ")

      if kullanici_sifre == Emre_Hesap["sifre"]:
        print(f"Hoşgeldiniz {Emre_Hesap['ad']}")
        atm_islem(Emre_Hesap)
        break
      elif kullanici_sifre == Ali_Hesap["sifre"]:
        print(f"Hoşgeldiniz {Ali_Hesap['ad']}")
        atm_islem(Ali_Hesap)
        break
      else:
        sayac -= 1
        if sayac == 0:
          print("Hakkınız bitti! Hesabınız bloke oldu.")
          return False
        print(f"Şifre yanlış! Kalan hak: {sayac}")

    elif giris_sekli == "QR":
      kullanici_kod = input("Lütfen telefonunuza gelen kodu giriniz: ")

      if kullanici_kod == Emre_Hesap["kod"]:
        print(f"Hoşgeldiniz {Emre_Hesap['ad']}")
        atm_islem(Emre_Hesap)
        break
      elif kullanici_kod == Ali_Hesap["kod"]:
        print(f"Hoşgeldiniz {Ali_Hesap['ad']}")
        atm_islem(Ali_Hesap)
        break
      else:
        sayac -= 1
        if sayac == 0:
          print("Hakkınız bitti! Hesabınız bloke oldu.")
          return False
        print(f"Kod yanlış! Kalan hak: {sayac}")

    else:
      print("Geçersiz seçim yaptınız!")
      break
atm_giris_sistemi()