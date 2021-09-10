try:
    print(x)
except:
    print("an exception occured")

a=[1,2,3]
try:
    print('2nd'+a[1])
    print('4th'+a[3])
except:
    print("error occured")

def fun(a):
    if a<4:
        b=a/(a-3)
        print("valueof b=",b)
try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("Zero Division Error occured and handled")
except NameError:
    print("name errror occured and handled")

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")

try:
    print("x")
except:
    print("went wrong")
finally:
    print("the try except is finished")

x=-1
if x<0:
    raise exception("no numbers below zero")

x='hello'
assert x=='bye','x should be hello
