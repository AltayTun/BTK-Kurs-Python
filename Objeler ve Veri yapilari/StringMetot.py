mesaj="Merhaba herkese . Benim adım Emre Altun"

mesaj= mesaj.upper()                    #Her harfin büyük yapar
mesaj= mesaj.lower()                    #Her harfi küçük yapar
mesaj= mesaj.title()                    #Her kelimenin baş harfini büyük yapar
mesaj= mesaj.strip()                    #Her kelimenin başındaki ve sonundaki boşlukları siler
mesaj= mesaj.capitalize()               #Sadece ilk harfi büyük yapar
mesaj= mesaj.split(".")                 #Her kelimeyi ayırır ve listeye atar
mesaj=" ".join(mesaj)                   #Her kelimeyi birleştirir
mesaj.find("Altun")                     #Aranan kelimenin kaçıncı indexte olduğunu verir. Bulamazsa -1 döndürür.
print(mesaj.index("Altun"))             #Aranan kelimenin kaçıncı indexte olduğunu verir. Bulamazsa hata verir.
print(mesaj)
isfound = mesaj.startswith("M")         #Aranan kelime ile başlıyorsa True, başlamıyorsa False döndürür.
print(isfound)
isfound = mesaj.endswith("n")           #Aranan kelime ile bitiyorsa True, bitmiyorsa False döndürür.
print(isfound)
mesaj= mesaj.replace("Emre","Ahmet")    #Aranan kelimeyi değiştirir.
# mesaj= mesaj.replace("ç ","c")
# .replace("ğ ","g")
# .replace("ı ","i")
# .replace("ö ","o")                     #Aranan kelimeyi değiştirir.
# .replace("ş ","s")
# .replace("ü ","u")          
mesaj=mesaj.center(100,"*")             #Mesajı ortalar ve boşlukları * ile doldurur.
