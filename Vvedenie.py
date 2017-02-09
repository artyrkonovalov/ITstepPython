Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> diff = 20
>>> diff
20
>>> load = diff * 5
>>> load
100
>>> diff = 5
>>> load
100
>>> load = diff * 5
>>> load
25
>>> a = 5
>>> b = 5
>>> a + b
10
>>> print(a + b)
10
>>> type(a)
<class 'int'>
>>> name = "Artyr"
>>> type(name)
<class 'str'>
>>> name = input("Enter name: ")
>>> 
>>> name = input('enter name: ')
enter name: Artyr
>>> name
'Artyr'
>>> type(name)
<class 'str'>
>>> name = ('Enter name')
>>> name = input("Enter name")
Enter name 123
>>> type(name)
<class 'str'>
>>> old
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    old
NameError: name 'old' is not defined
>>> old = int(input("how old are yuo"))
how old are yuo 33
>>> type(old)
<class 'int'>
>>> old = int(input('old')
	  old 33.5
	  
SyntaxError: invalid syntax
>>> type(int(input('old')
	 old33
	 
SyntaxError: invalid syntax
>>> type(int(input('old')))
old33
<class 'int'>
>>> 2**8
256
>>> pow(2,8)
256
>>> abs(-9)
9
>>> 36%5
1
>>> type(float(input('old')))
old33,5
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    type(float(input('old')))
ValueError: could not convert string to float: '33,5'
>>> type(float(input('old')))
old33.5
<class 'float'>
>>> float(5)
5.0
>>> true
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> True
True
>>> type(True)
<class 'bool'>
>>> 5+True
6
>>> 0e5
0.0
>>> 23e5
2300000.0
>>> 23e-5
0.00023
>>> 
