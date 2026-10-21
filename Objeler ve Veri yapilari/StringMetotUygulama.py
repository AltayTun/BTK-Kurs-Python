website="http://www.sadikturan.com"
course="Python Kursu: Baştan sona python programlama rehberiniz (40 saat)"

# 1-"Hello World" karakter dizisinin baş ve sodnaki boşlukları silin.
x="Hello World"
x=x.strip()
print(x)
# 2-"www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.
result="www.sadikturan.com".strip("w.moc")
# 3-"course" karakter dizisinin tüm karakterlerini küçük harf yapın.
course=course.lower()
print(course)
# 4-"website" karakter dizisinin içinde kaç tane a karakteri vardır.
a_sayisi=website.count("a")
print(a_sayisi)
# 5-"website" karakter dizisinin www ile başlayıp com ile bitip bitmediğini kontrol edin.
a=website.startswith("www")
print(a)
b=website.endswith("com")
print(b)
# 6-"website" içinde ".com" ifadesi var mı kontrol edin.
y=website.find(".com")
print(y)
# 7-"course" içindeki karakterleri hepsi alfabetikmi kontrol edin.(isalpha, isdigit)
c=course.isalpha()
print(c)
# 8-"Contents" ifadesinin satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyin.
contents="Contents"
contents=contents.center(50,"*")
print(contents)
# 9-"course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin.
course="-".join(course)
print(course)
# 10-"Hello World" karakter dizisinin "World" ifadesini "There" ile değiştirin.
course=course.replace("World","There")
print(course)
# 11-"course" karakter dizisini boşluk karakterlerinden ayırın.
course=course.split()
print(course)