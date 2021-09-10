#1
name="earth"
name_comp=[var for var in name]
print(name_comp)

#2
list1=["M","na","i","Ke"]
list2=["y","me","s","lly"]
list_comp=[var for var in zip(list1,list2)]
print(list_comp)

#3
alist=[1,2,3,4,5,6,7]
list3=[var**2 for var in range(1,8)]
print(list3)

#4
sampleDict={"name":"kelly","age":25,"salary":8000,"city":"New york"}
dict=[key for key in sampleDict]
print(dict)

#5

#6
def sum(n):
    total=0
    for x in n:
        total+=x
    return total
print(sum([2,10,5,20,40]))

#7
def prime(n):
    for x in range(2,n):
        if n % x == 0:
            print("not prime")
            break
    else:
        print("prime")
n=int(input("enter a no:"))
print(prime(n))

#8
def palindrom(str):
    s1=str[::-1]
    if str==s1:
        print("palindrome")
    else:
        print("not palindrom")
print(palindrom("malayalam"))

#9
mylist=[1,2,3,4,5,6]
new=list(filter(lambda x:(x%2==0),mylist))
print(new)

#10
def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str.lower():
         return False
   return True

string = 'The five boxing wizards jump quickl.'
if(ispangram(string) == True):
   print("Yes")
else:
   print("No")






