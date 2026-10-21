def square(num):return num **2
numbers=[1,3,5,9]
result=list(map(square,numbers))
print(result)

for item in (map(square,numbers)):
    print(item)


#def square(num):return num **2
numbers=[1,3,5,9]
result=list(map(lambda num: num**2,numbers))
print(result)

#for item in (map(square,numbers)):
#print(item)

#Yukardaki işlemle tamamen aynı
square=lambda num:num**2

print(result)


# def square(num): return num ** 2
#square=lambda num: num ** 2
numbers = [1,4,5,10]
# result = list(map(lambda num: num **2, numbers))
# result = list(map (square, numbers))
result=square(3)
# for item in map(square, numbers):
# print(item)
#print(result)

check_event=lambda num:num%2==0
#def check_event(num):return num%2==0       
#result=list(filter(check_event,numbers))
result=list(filter(check_event,numbers))
#result=list(filter(lambda num:num%2==0,numbers))
result=check_event(numbers[2])

print(result)