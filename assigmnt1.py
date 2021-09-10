#1
myList = [1, 2,3,4,5,6,7]
print(myList)
temp = myList[-1]
myList[-1] = myList[0]
myList[0] = temp
print(myList)

#2
list=[100,10,40,50]
list.sort()
print(list[0])

#3
a=[1,2,3,4,5,6,7,8]
for num in a:
    if num%2==0:
        print(num)

#4
b=[1,2,3,4,5,6,7,8]
for m in b:
    if num%2!=0:
        print(m)

#5
c=[-1,1,-2,2,-3,3]
for n in c:
    if num>=0:
        print(n)

#6
d=[-1,1,-2,2,-3,3]
for p in d:
    if num<=0:
        print(p)

#7
Fahrenheit= 54  
Celsius = ((Fahrenheit-32)*5)/9  
print("Temperature in Celsius is: ");  
print(Celsius);

#8
tuple=(3,1,7,3,9,6)

print("maximum number in a tuple is:",max(tuple))
print("minimum number in a tuple is:",min(tuple))

#9
list1=[1,2,10,5]
tuple=tuple(list1)
print(tuple)

#10
list2=[10,20,30,40]
list2.append(50)
print(list2)
list3=[100,200,300,400]
list4=[500,600,700,800]
list3.extend(list4)
print(list3)
print(len(list3))
