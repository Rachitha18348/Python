Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d"%(a,b))
after swapping a=20,b=10
a=5.6
b=8.9
print("after swapping a=%f,b=%f"%(a,b))
after swapping a=5.600000,b=8.900000
print("after swapping a=%.2f,b=%.2f"%(a,b))
after swapping a=5.60,b=8.90
a="python"
b-"java"
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b-"java"
TypeError: unsupported operand type(s) for -: 'float' and 'str'
b="java"
print("after swapping a=s%,b=s%"%(a,b))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print("after swapping a=s%,b=s%"%(a,b))
ValueError: unsupported format character ',' (0x2c) at index 19
a,b=b,a
print("after swapping a=s%,b=s%"%(a,b))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print("after swapping a=s%,b=s%"%(a,b))
ValueError: unsupported format character ',' (0x2c) at index 19
print("after swapping a=%s,b=%s"%(a,b))
after swapping a=java,b=python

#list[]
a=[2,4.5,7+5j,"python",True,False]
a
[2, 4.5, (7+5j), 'python', True, False]
type(a)
<class 'list'>
b=7.8
type(b)
<class 'float'>
c=[7.8]
type(c)
<class 'list'>
a=['python','java','c','c++']
a.append("class")
a
['python', 'java', 'c', 'c++', 'class']
a.append(['ds','ml'])
a
['python', 'java', 'c', 'c++', 'class', ['ds', 'ml']]
#extend
a.extend(['AI','DL'])
a
['python', 'java', 'c', 'c++', 'class', ['ds', 'ml'], 'AI', 'DL']
#insert
a.insert(3,"Fullsatck')
         
SyntaxError: unterminated string literal (detected at line 1)
a.insert(3,'fullstack')
         
a
         
['python', 'java', 'c', 'fullstack', 'c++', 'class', ['ds', 'ml'], 'AI', 'DL']
#index
         
a.index('java')
         
1
#copy()
         
a.copy()
         
['python', 'java', 'c', 'fullstack', 'c++', 'class', ['ds', 'ml'], 'AI', 'DL']
a
         
['python', 'java', 'c', 'fullstack', 'c++', 'class', ['ds', 'ml'], 'AI', 'DL']
b=a.copy()
         
b
         
['python', 'java', 'c', 'fullstack', 'c++', 'class', ['ds', 'ml'], 'AI', 'DL']
#clear
         
a.clear()
         
a
         
[]
a=b.copy()
         

a
         
['python', 'java', 'c', 'fullstack', 'c++', 'class', ['ds', 'ml'], 'AI', 'DL']
b
         
['python', 'java', 'c', 'fullstack', 'c++', 'class', ['ds', 'ml'], 'AI', 'DL']
#sort()
         
a={"apple","mango",'orange']
         
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a=["apple","mango",'orange']
         
a.sort()
         
a
         
['apple', 'mango', 'orange']
a=[9,3,6,2,5]
         
a
         
[9, 3, 6, 2, 5]
a.sor()
         
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.sor()
AttributeError: 'list' object has no attribute 'sor'. Did you mean: 'sort'?
a.sort()
         
a
         
[2, 3, 5, 6, 9]
#reverse
         
a.reverse()
         
>>> a
...          
[9, 6, 5, 3, 2]
>>> #pop - to delete in list
...          
>>> #remove-to delete
...          
>>> a=[2,3,6,3,5]
...          
>>> a.pop()
...          
5
>>> 
>>> a
...          
[2, 3, 6, 3]
>>> a.pop(4) #need index of the number which should be deleted
...          
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.pop(4) #need index of the number which should be deleted
IndexError: pop index out of range
>>> a.pop(1)
...          
3
>>> a
...          
[2, 6, 3]
>>> a.remove(6)
...          
>>> a
...          
[2, 3]
>>> #count
...          
>>> a=[2,3,5,6,3,6,8,6,9,3,6]
...          
>>> a.count(3)
...          
3
>>> a.count(6)
...          
4
>>> len(a)
...          
11
