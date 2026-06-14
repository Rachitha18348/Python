Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set

s={}
print(type(s))
<class 'dict'>

a=set() #to create a empty set
print(type(a))
<class 'set'>

a=set({10,1,2,3})
print(a)
{10, 1, 2, 3}
a=set({10,1,2,3,3})
print(a)
{10, 1, 2, 3}
print(a[0])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(a[0])
TypeError: 'set' object is not subscriptable
print(a[0])  #index is not possible
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(a[0])  #index is not possible
TypeError: 'set' object is not subscriptable
s={True,1}
s
{True}
s={1,True}
s
{1}
s={1,2,3,4,True,"name"}
s
{1, 2, 3, 4, 'name'}
#adding e;ement to the set
s.add(20)
print(s)
{1, 2, 3, 4, 20, 'name'}
#only single element can be added in set
s.add(0)
s
{0, 1, 2, 3, 4, 20, 'name'}
s.add(False)
s
{0, 1, 2, 3, 4, 20, 'name'}
s.update({12,34,"hi"})
s
{0, 1, 2, 3, 4, 34, 12, 20, 'hi', 'name'}
#update is used to add more than one element

#to remove elements
print(s.pop())
0
s
{1, 2, 3, 4, 34, 12, 20, 'hi', 'name'}
s.remove("name")
s
{1, 2, 3, 4, 34, 12, 20, 'hi'}
s.discard(1)
s
{2, 3, 4, 34, 12, 20, 'hi'}

s.discard(34)
>>> s
{2, 3, 4, 12, 20, 'hi'}
>>> s.clear()
>>> s
set()
>>> a={2,3,4,"python"}
>>> s=set(map(int,input().split()))
2 3 4 5 6 7
>>> s
{2, 3, 4, 5, 6, 7}
>>> min(s)
2
>>> max(s)
7
>>> sum(s)
27
>>> 
>>> 
>>> s1={1,2,3,4,5,6}
>>> s2={4,5,6,7,8,9)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> s1={1,2,3,4,5,6}
>>> s2={4,5,6,7,8,9}
>>> print(s1.union(s2))
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> print(s1.intersection(s2))
{4, 5, 6}
>>> print(s1|s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> print(s1&s2)
{4, 5, 6}
>>> print(s1.difference(s2))
{1, 2, 3}
>>> print(s2-s1)
{8, 9, 7}
>>> print(s1^s2)
{1, 2, 3, 7, 8, 9}
>>> print(s1.issubset(s2))
False
>>> print(s2>=s1)
False
>>> print(s1.issuperset(s2))
False
>>> print(s1.isdisjoint(s2))
False
