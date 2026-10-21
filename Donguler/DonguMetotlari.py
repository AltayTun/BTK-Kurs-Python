#range
for item in range(2,10,2):
    print(item)

for item in range(3):
    print(f"**********")

print(list(range(2,10,2)))


for item in range(3):
    print(f"**********")

#enumerate

index=0
mesaj="Hello there"

for letter in mesaj:
    print(f"index:{index} letter:{mesaj[index]}")
    index+=1

for item in range(3):
    print(f"**********")

greeting = 'Hello there'
for index,letter in enumerate (greeting):
    print(f'index: {index} letter: {greeting [index]}')

for item in range(3):
    print(f"**********")

greeting = 'Hello there'
for item in enumerate (greeting):
    print(item)

for item in range(3):
    print(f"**********")

#zip

list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]

print(list(zip(list1,list2,list3)))
for item in range(3):
    print(f"**********")

for item in zip(list1,list2,list3):
    print(item)

for item in range(3):
    print(f"**********")

for a,b,c in zip(list1,list2,list3):
    print(a)

islem_gecmisi = ["Para Yatırma", "EFT Gönderimi", "Fatura Ödemesi"]

print("--- HESAP HAREKETLERİ ---")
for no, islem in enumerate(islem_gecmisi, start=1):
    print(f"{no}. İşlem: {islem}")