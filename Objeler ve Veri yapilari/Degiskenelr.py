maasAli=5000
maasAhmet=4000
vergiOrani=0.27
print("maasAli:", maasAli   -   (maasAli   * vergiOrani))
print("maasAhmet:", maasAhmet -   (maasAhmet * vergiOrani))

# Değişken tanımlama kuralları
# Rakam ile başlıyamaz
number1=10
print("number1 1.:", number1)

number1=20
print("number1 2.:", number1)

number1+=30
print("number1 3.:", number1)


age=20
AGE=30
print("age:", age)
print("AGE:", AGE)

#Türkçe karakter kullanılmaz
yas=20
_age=30
print("yas:", yas)
print("_age:", _age)

x=1             #int       
y=2             #int
name="Çınar"    #string
isStudent=False #boolean

x,y,name,isStudent=1,2,"Çınar",False

a="10"
b="20"
print(a+b) #30 olmaz => 1020 olur çünkü string olarak birleştirir.

firstName="Ali"
lastName="Veli"
print(firstName + " " + lastName) #Ali Veli
