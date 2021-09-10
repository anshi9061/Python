#dictionary
#1
mydict={"fruit":"apple","color":"red","seed":"yes"}
print(mydict)

#2
thisdict={"vegetable":"onion"}
mydict.update(thisdict)
print(mydict)

#3
dict={"a":100,"b":200}
x=input("enter the key:")
if x in dict:
    print("key present")
else:
    print("not present")

#4
mydict.pop("fruit")
print(mydict)

#5
x={1:10,2:20}
y={3:30,4:40}
z={5:50,6:60}
x.update(y)
print(x)
x.update(z)
print(z)

#set
#6
myset={100,200,300}
print(myset)

#7
myset.remove(100)
print(myset)

#8
aset={1,2,3,4}
bset={2,3,5,6}
aset.intersection_update(bset)
print(aset)

#9
cset=aset.union(bset)
print(cset)

#10
aset.symmetric_difference_update(cset)
print(aset)



