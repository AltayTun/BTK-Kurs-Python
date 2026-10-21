# key - value

# 41 => kocaeli 34 =>İstanbul

# 1. YÖNTEM: İki Ayrı Liste İle İndeks Üzerinden Erişim
sehirler = ["Kocaeli", "İstanbul"]
plakalar_listesi = [41, 34]

# sehirler.index("Kocaeli") -> 0 döndürür. plakalar_listesi[0] -> 41 basar.
print(plakalar_listesi[sehirler.index("Kocaeli")])  # Çıktı: 41


# 2. YÖNTEM: Sözlük (Dictionary) Kullanımı (Tavsiye Edilen)
plakalar = {
    "Kocaeli": 41,
    "İstanbul": 34
}

# Sözlük üzerinden eleman çağırma (Büyük/küçük harfe dikkat)
print(plakalar["Kocaeli"])   # Çıktı: 41
print(plakalar["İstanbul"])  # Çıktı: 34

# Yeni anahtar-değer ekleme
plakalar["Ankara"] = 6

# Var olan bir değeri güncelleme
plakalar["Kocaeli"] = "yeni değer"

# Sözlüğün son halini ekrana basma
print(plakalar)
# Çıktı: {'Kocaeli': 'yeni değer', 'İstanbul': 34, 'Ankara': 6}
# users={
#     "sadikturan":
#     {
#         "age":36,
#         "roles":["user"],
#         "email":"sadik@gmail.com",
#         "phone":"12312415"
        
#     },
#     "cinarturan":
#     {
#         "age":2,
#         "roles":["admin","user"],
#         "email":"cinar@gmail.com",
#         "phone":"12397940"
#     }
# }
# print(users["cinarturan"])
# print(users["cinarturan"]["age"])
# print(users["cinarturan"]["roles"])

