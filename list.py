Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list=[1,4,6,3,7,1]
>>> list.insert(1,55)
>>> print(list)
[1, 55, 4, 6, 3, 7, 1]
>>> list.pop(0)
1
>>> print(list)
[55, 4, 6, 3, 7, 1]
>>> list.append(11)
>>> print(list)
[55, 4, 6, 3, 7, 1, 11]
>>> list.sort()
>>> print(list)
[1, 3, 4, 6, 7, 11, 55]
>>> list.pop()
55
>>> print(list)
[1, 3, 4, 6, 7, 11]
>>> list.sort(reverse=True)
>>> print(list)
[11, 7, 6, 4, 3, 1]
>>> 