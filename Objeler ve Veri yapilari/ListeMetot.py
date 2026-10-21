numbers=[1,10,5,16,4,9,10]
letters=["a","g","s","b","y","a","s"]

val=min(numbers)
print(val)
val=max(numbers)
print(val)
kal=min(letters)
print(kal)
kal=max(letters)
print(kal)

val=numbers[3:6]     #3 ile 6 arasındaki 3 ifadeyi alır
print(val)
val=numbers[:3]      #ilk 3 ifadeyi alır
print(val)
val=numbers[4:]      #4.Terimden başlıyarak sona kadar gider
print(val)

numbers[4]=40        #4 elemanının yerine 40 yazar
print(numbers)

numbers.append(49)   #Sona eleman ekler
print(numbers)

numbers.insert(3,78) #İstediğimiz indexe eleman ekler
print(numbers)

numbers.pop(3)       #İstediğimiz indexteki elemanı siler
print(numbers)

numbers.remove(59)   #İstediğimiz karakteri siler
print(numbers)

numbers.sort()       #Sıralama yapar
print(numbers)

numbers.reverse()    #Ters Çevirir
print(numbers)

print(len(numbers))  #Kaç elemanlı olduğunu söyler
print(numbers.count(10)) #O eleamndan kaç tane olduğunu söyler

numbers.clear()      #Bütün elemanları siler
print(numbers)