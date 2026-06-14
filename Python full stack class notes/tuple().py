Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(4,9.8,"python",7+j,True,False)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a=(4,9.8,"python",7+j,True,False)
NameError: name 'j' is not defined
>>> a=(4,9.8,"python",7+2j,True,False)
>>> type(a)
<class 'tuple'>
>>> a.count(4)
1
>>> a.index("python")
2
>>> len(a)
6
