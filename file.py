#1
'''f=open("poem.txt","w")
f.write(input("enter a number"))
f.close()'''

#2
a=open("poem1.txt","w")
a.write("twinkle twinkle,little star\n"
         "how i wonder what you are \n"
         "up above the world of high \n"
        "like a diamond inthe sky \n")
a.close()

#3
a=open("poem1.txt","r")
p=a.readlines()
print(p)

#4
a=open("poem1.txt","r")
p=a.readline()
print(p)

#5
b= open("poem1.txt", "r")
count=0
for line in b:
    if line != "\n":
        count += 1
b.close()

print(count)

