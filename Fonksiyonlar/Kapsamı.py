# Global scope
x="Global x"

def function():
    #local scope
    #x="Local x"
    print(x)      #Fonksiyon kapsamında ve Global kapsamında

function()
print(x)          #Global kapsamında

#################################
print("-"*50)

#Global
name="Çınar"
def changeName(new_name):
    #Local
    name=new_name
    print(name)
changeName("Ada")
print(name)

##################################
print("-"*50)


name=" global string"

def greeting():
    #name="Çınar"

    def hello():
        #name="Ada"
        print("hello" + name)   #Bir üstteki fonksiyonun değerini alır bir değer belirtilmemişse
    hello()

greeting()
###################################
print("-"*50)



x=50
def test(x):
    print(f"x:{x}")
    x=100
    print(f"Changed x to {x}" )

test(x)
print(x)


#global x'i içerden değiştirme
x=50
def test():
    global x
    print(f"x:{x}")
    x=100
    print(f"Changed x to {x}" )

test()
print(x)