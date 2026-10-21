# 1-100 e kadar sayıları ekrana yazdırımı

x = 1

while x <= 100:
    if x % 2 == 0:
        print(f"sayı çift: {x}")
    else:
        print(f"sayı tek: {x}")
    
    x = x + 1  # x'i döngünün İÇİNDE artırmalısın ki sonsuz döngüye girmesin!

print("bitti")

name = ""  # false
while not name.stirp():
    name = input("isminizi giriniz:")

print(f"Merhaba {name}") 