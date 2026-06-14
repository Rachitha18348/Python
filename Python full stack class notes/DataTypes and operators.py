<<<<<<< HEAD
Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data Types
a=1
type(a)
<class 'int'>
b=9.9
type(b)
<class 'float'>
c="python"
type(c)
<class 'str'>
type(b)
<class 'float'>
d='code'
type(d)
<class 'str'>
a=3j+2
type(a)
<class 'complex'>
d=True
type(d)
<class 'bool'>
#DataType Conversions
int(8)
8
int(8.8)
8
int("python")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(8+9j)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(8+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
float(1)
1.0
float(9.9)
9.9
float("python")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
float(3+9j)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(3+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
str(1)
'1'
str(3.3)
'3.3'
str("python")
'python'
str(3j)
'3j'
str(True)
'True'
complex(1)
(1+0j)
complex("python")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
complex(8j)
8j
complex(True)
(1+0j)
bool(1)
True
bool(2.2)
True
bool('python')
True
bool(5j)
True
bool(True)
True
bool(False)
False
#arthematic operators
a=3
b=9
print(a+b)
12
print(a-b)
-6
print(a*b)
27
print(a//b)
0
print(a/b)
0.3333333333333333
print(a**b)
19683
print(b**a)
729
print(a%b)
3
print(b%a)
0
#assignment operators
a=5
b=9
a+=b
a
14
a*=b
a
126
a-=d
a
125
a/=b
a
13.88888888888889
a**=20
a
7.134278705968649e+22
#comparision operators

a=9
b=3
a<b
False
a>b
True
a<=b
False
b>=b
True
a!=b
True
a==b
False
#logical operators
a=9
b=8
a<b and b<a
False
a<b and b>a
False
a>b and b>a
False
a>b and b<a
True
not True
False
not false
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    not false
NameError: name 'false' is not defined. Did you mean: 'False'?
not False
True
a!=b or a==b
True
#identify operators
a=6
if type(a) is int:
    print("integer")
else:
    print("not integer")

    
integer
a=9
>>> a
9
>>> str="python"
>>> if type(str) is str:
...    print("It is String")
... else:
...     print("It is not String")
... 
...     
It is not String
>>> a="python"
>>> if type(a) is str:
...     print("It is String")
... else:
...     print("Not")
... 
...     
Not
>>> #membership operators
>>> a=2,3,4,5,6,7
>>> if 7 in a:
...     print(7)
... 
...     
7
>>> if 20 in a:
...     print(20)
... 
...     
>>> 
>>> if 20 not in a:
...     print(20)
... 
...     
20
>>> a="python","java","C"
>>> if "C" in a:
...     print("true")
... 
...     
true
>>> if "C" not in a:
...     print("false")
... 
...     
>>> 
=======
Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data Types
a=1
type(a)
<class 'int'>
b=9.9
type(b)
<class 'float'>
c="python"
type(c)
<class 'str'>
type(b)
<class 'float'>
d='code'
type(d)
<class 'str'>
a=3j+2
type(a)
<class 'complex'>
d=True
type(d)
<class 'bool'>
#DataType Conversions
int(8)
8
int(8.8)
8
int("python")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(8+9j)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(8+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
float(1)
1.0
float(9.9)
9.9
float("python")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
float(3+9j)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(3+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
str(1)
'1'
str(3.3)
'3.3'
str("python")
'python'
str(3j)
'3j'
str(True)
'True'
complex(1)
(1+0j)
complex("python")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
complex(8j)
8j
complex(True)
(1+0j)
bool(1)
True
bool(2.2)
True
bool('python')
True
bool(5j)
True
bool(True)
True
bool(False)
False
#arthematic operators
a=3
b=9
print(a+b)
12
print(a-b)
-6
print(a*b)
27
print(a//b)
0
print(a/b)
0.3333333333333333
print(a**b)
19683
print(b**a)
729
print(a%b)
3
print(b%a)
0
#assignment operators
a=5
b=9
a+=b
a
14
a*=b
a
126
a-=d
a
125
a/=b
a
13.88888888888889
a**=20
a
7.134278705968649e+22
#comparision operators

a=9
b=3
a<b
False
a>b
True
a<=b
False
b>=b
True
a!=b
True
a==b
False
#logical operators
a=9
b=8
a<b and b<a
False
a<b and b>a
False
a>b and b>a
False
a>b and b<a
True
not True
False
not false
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    not false
NameError: name 'false' is not defined. Did you mean: 'False'?
not False
True
a!=b or a==b
True
#identify operators
a=6
if type(a) is int:
    print("integer")
else:
    print("not integer")

    
integer
a=9
>>> a
9
>>> str="python"
>>> if type(str) is str:
...    print("It is String")
... else:
...     print("It is not String")
... 
...     
It is not String
>>> a="python"
>>> if type(a) is str:
...     print("It is String")
... else:
...     print("Not")
... 
...     
Not
>>> #membership operators
>>> a=2,3,4,5,6,7
>>> if 7 in a:
...     print(7)
... 
...     
7
>>> if 20 in a:
...     print(20)
... 
...     
>>> 
>>> if 20 not in a:
...     print(20)
... 
...     
20
>>> a="python","java","C"
>>> if "C" in a:
...     print("true")
... 
...     
true
>>> if "C" not in a:
...     print("false")
... 
...     
>>> 
>>>>>>> d4f8f21c657bb527d926585f6f410478cea322ed
