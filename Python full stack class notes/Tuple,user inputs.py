Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple()

x=(1,2,0.01)
print(x)
(1, 2, 0.01)
print(type(x))
<class 'tuple'>
>>> print(x[0],x[1])
1 2
>>> print(x[-2],x[-1])
2 0.01
>>> print(min(x))
0.01
>>> print(max(x))
2
>>> print(sum(x))
3.01
>>> print(x[1:])
(2, 0.01)
>>> print(x[::-1])
(0.01, 2, 1)
>>> 
>>> 
>>> 
>>> #user input()
>>> 
>>> x=input("enter name:")
enter name:rachitha
>>> print(x,type(x))
rachitha <class 'str'>
>>> a=int(input())
3
>>> print(a,type(a))
3 <class 'int'>
>>> b=float("num:")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b=float("num:")
ValueError: could not convert string to float: 'num:'
>>> b=float(input("num:"))
num:23.89
>>> print(b,type(b))
23.89 <class 'float'>
>>> c=complex(input())
4
>>> print(c,type(c))
(4+0j) <class 'complex'>
>>> d=bool(input())
3
>>> print(d)
True
>>> name=input("name:")
name:rachitha
