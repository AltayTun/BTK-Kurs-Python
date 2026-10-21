#class
class Person:
    address = "no information"
    #attributes
    # class attributes

    #constructor (yapıcı method)
    def __init__(self,name,year):   #Classtan tanımlanan herhangi bir objeyi temsil eder
        
        # object attributes
        self.name=name
        self.year=year
        print("init metodu çalıştı")

    
    # instance methods
    def intro(self):
        print("Hello there.I am" + self.name),
    
    # instance methods
    def calculataAge(self):
        return 2019-self.year


#object(instance)
p1=Person(name="Emre",year=1990)
p2=Person(name="Çağatay",year=1995)

p1.intro()
p2.intro()

print(f"adım:{p1.name} ve yaşım: {p1.calculataAge()}")
print(f"adım:{p2.name} ve yaşım: {p2.calculataAge()}")
#updating
p1.name="ahmet"
p1.address="kocaeli"
#accessing object attributes
print(f"p1 :name:{p1.name} year:{p1.year} addres:{p1.address}")
print(f"p2 :name:{p2.name} year:{p2.year} addres:{p2.address}")

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1==p2)



class Circle:
  # Class object attribute
  pi = 3.14

  def __init__(self, yaricap=1):
    self.yaricap = yaricap

  # methods
  def cevre_hesapla(self):
    return 2 * self.pi * self.yaricap  

  def alan_hesapla(self):
    return self.pi * (self.yaricap**2)


c1 = Circle()  # yarıçap = 1
c2 = Circle(5)  # yarıçap = 5

# Metotların sonuna () eklendi ve ikinci print c2 olarak düzeltildi
print(f"c1: alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}")
print(f"c2: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}")