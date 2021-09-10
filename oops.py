#class
class simple:
    def hai(self):
        print("hai")

a=simple()
a.hai()

#constructor
class welcome:
    def __init__(self,name):
        self.name=name

    def display(self):
        print("name:" +self.name)
x=welcome("Ansheena")
x.display()

#destructors
class world:
    def __init__(self):
        print("Amazing world")
    def __del__(self):
        print("destructed called,world deleted")
obj=world()
del obj

#simple inheritance
class Baseclass:
    def display(self):
        print("hello")

class subclass(Baseclass):
    def welcome(self):
        print("welcome")

y=subclass()
y.display()
y.welcome()

#multiple inheritance
class first:
    def display(self):
        print("first")

class second:
    def display_second(self):
        print("second")

class third(first,second):
    def display_third(self):
        print("third")

x=third()
x.display_third()
x.display_second()
x.display()

#hierarchial
class calculator:
    def sum(self,a,b):
        return a+b
    
class derived1(calculator):
    def mul(self,a,b):
        return a*b

class derived2(calculator):
    def div(self,a,b):
        return a/b

ob1=derived1()
ob2=derived2()
print(ob1.sum(2,3))
print(ob1.mul(2,3))
print(ob2.div(2,3))
print(ob2.sum(2,3))


        
    
