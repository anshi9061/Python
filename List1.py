#list
#1
list=[1,4,6,3,7,1]
list.insert(1,55)
print(list)
list.pop(0)
print(list)
list.append(11)
print(list)
list.sort()
print(list)
list.pop()
print(list)
list.sort(reverse=True)
print(list)

#2
list=[2,10,5,7,9,4]
list.sort()
print(list)
print("largest number is:",list[-1])

#3
a=[8,7,5,2,1,4]
b=[1,3,6,10,19]
a.extend(b)
print(a)
a.sort()
print(a)

#string
#1
hai="engineering"
print(hai)
print(hai.replace("g",""))

#2
hloo="ansheena"
print(hloo.replace("a","$"))

#3
x="Anshi"
print(x.isalnum())
print(x.isalpha())
print(x.isdigit())
print(x.islower())
print(x.isupper())

#4
x="abc"
y="xyz"
x1=y[:2]+x[2:]
y1=x[:2]+y[2:]
print(x1+" "+y1)


#tuple
#1
tuple=("anshi",3,"ksd")
print(tuple)

#2
print(tuple[2])

#3 cannot be executable

#4
print(tuple.index("anshi"))








