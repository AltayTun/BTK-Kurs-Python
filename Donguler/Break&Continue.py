# isim="sadık turan"

# for letter in isim:
#     if letter=="t":
#         break      #o kısma geldiği zaman döngü durur
#     print(letter)
# print("*******************")


# for letter in isim:
#     if letter=="a":
#         continue    #o kısma geldiği zaman es geçer
#     print(letter)
# x=0
# while x<5:
#     if x==2:
#         continue
#     print(x)
#     x+=1

#1-100 e kadar tek sayıların toplaı

x=1
toplam=0
while x<=100:
    x+=1
    if x % 2 ==1:
        continue
    toplam+=x
print(f"toplam:{toplam}")
