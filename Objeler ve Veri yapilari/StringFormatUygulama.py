website="http://www.sadikturan.com"
course="Python Kursu: Baştan sona python programlama rehberiniz (40 saat)"
print("website karakter sayısı:",len(website))
# 1- "course" karakter dizisinde kaç karakter bulunmaktadır?
print("Kursun karakter sayısı:",len(course))
# 2- "website" içinden www karakterlerini alın.
print("www karakterlerinin göstrerimi:",website[7:10])
# 3- "website" içinden com karakterlerini alın.
print("com karakterlerinin gösterimi:",website[22:25])
# 4- "course" içinden ilk 15 ve son 15 karakterlerini alın.
print("İlk 15 karakter",course[0:15])
print("Son 15 karakter:",course[49:65])
# 5- "course" içindeki karakterleri tersten yazdırın.
print("course içindekileri tersten yazımı",course[::-1])

name,surname,age,job="Bora","Yılmaz",32,"Mühendis"

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyei yazdırın.
#     "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis"
print(f"Benim adım {name} {surname},Yaşım {age} ve mesleğim {job}.")
# 7- "Hello world" ifadesindeki w harfini "W"ile değiştirin
s="Hello world"
result=s[6]
s=s[0:6]+"W"+s[-4]
print(s)
# 8- "abc" ifadesinin yan yana 3 defa yazdırın
print("abc"*3)