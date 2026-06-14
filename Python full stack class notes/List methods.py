Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#List Methods

a=[1,2,3]
print(a)
[1, 2, 3]
a.ppend(10)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.ppend(10)
AttributeError: 'list' object has no attribute 'ppend'. Did you mean: 'append'?
a.append(10)
print(a)
[1, 2, 3, 10]
a.index(10)
3
print(a.extend([5,7,8]))
None
a.extend([5,7,8])
print(a)
[1, 2, 3, 10, 5, 7, 8, 5, 7, 8]
a.insert(2,9)
print(a)
[1, 2, 9, 3, 10, 5, 7, 8, 5, 7, 8]
a.insert(4,[23,56])
print(a)
[1, 2, 9, 3, [23, 56], 10, 5, 7, 8, 5, 7, 8]
a=[1,'code','program','sai','ram','2.0']
print(a[0:5:2])
[1, 'program', 'ram']
a.extend([99,98)]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a.extend([99,98])
print(a)
[1, 'code', 'program', 'sai', 'ram', '2.0', 99, 98]
a.insert(4,"prom")
print(a)
[1, 'code', 'program', 'sai', 'prom', 'ram', '2.0', 99, 98]
print(a.pop())
98
print(a)
[1, 'code', 'program', 'sai', 'prom', 'ram', '2.0', 99]
print(a.pop(3))
sai
print(a)
[1, 'code', 'program', 'prom', 'ram', '2.0', 99]
a.remove('code')
print(a)
[1, 'program', 'prom', 'ram', '2.0', 99]
>>> 
>>> a.clear()
>>> print(a)
[]
>>> 
>>> a=[1,2,3]
>>> b=a.copy()
>>> print(a)
[1, 2, 3]
>>> print(b)
[1, 2, 3]
>>> 
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> a=[0,2,3,8,6,5]
>>> a.reverse()
>>> print(a)
[5, 6, 8, 3, 2, 0]
>>> a.sort()
>>> print(a)
[0, 2, 3, 5, 6, 8]
>>> a=[2,1,4,3,6]
>>> a.sort(reverse=True)
>>> print(a)
[6, 4, 3, 2, 1]
>>> a.sorted()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> print(sorted(a))
[1, 2, 3, 4, 6]
>>> #sorted(a) is used for temporary
>>> 
>>> print(min(a))
1
>>> print(max(a))
6
>>> print(sum(a))
16
