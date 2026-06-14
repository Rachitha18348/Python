<<<<<<< HEAD
Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#upper()
#lower()
#captialize()
#title()
a="python course"
a.uper()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.uper()
AttributeError: 'str' object has no attribute 'uper'. Did you mean: 'upper'?
a.upper()
'PYTHON COURSE'
a="CODEGNAN"
a.lower()
'codegnan'
a="python course"
a.captialize()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
a.capitalize()
'Python course'
a.title()
'Python Course'

a="code"
a.isupper()
False
a.islower()
True
a.isalpha()
True
b="code gnan"
b.isalpha()
False
b="codegnan"
b.isalpha()
True
b=1234
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
b="1234"
b.isdigit()
True
a="rachitha123"
a.isalnum()
True
a="rac@123"
a.isalnum()
False

#split()
#join()
a="python java C C++"
a.split()
['python', 'java', 'C', 'C++']
b="i","am","learning"
"".join(b)
'iamlearning'
" ".join(b)
'i am learning'
#concatenation
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
print((a+" "+b).title())
Python Course
#formating
a=2
b=4
print("the sum of a and b is:",a+b)
the sum of a and b is: 6
#Dot Formating
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu
print("hello {}\nhello {}".format(a,b))
hello motu
hello patlu
#fstring

a="chota"
b="bheem"
print(f"hello {a}{b})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f"hello {a}{b}")
      
hello chotabheem
print(f"hello {a} {b}")
      
hello chota bheem
print(f"hello {a}hello{b}")
      
hello chotahellobheem
print((f"hello {a} hello{b}")).title()
      
hello chota hellobheem
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print((f"hello {a} hello{b}")).title()
AttributeError: 'NoneType' object has no attribute 'title'
print(f"hello {a}\nhello{b}")
      
hello chota
hellobheem
a=3
      
b=8
      
c=axb
      
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    c=axb
NameError: name 'axb' is not defined
c=a*b
      
a=4
      
b=5
      
print("product is {}{}".format(a*b))
      
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print("product is {}{}".format(a*b))
IndexError: Replacement index 1 out of range for positional args tuple
c=a*b
      
print("product is {}".format(c))
      
product is 20
print(f"product is{c}")
      
product is20
print(f"product is {c}")
      
product is 20

#Swapping of two variables
      
a=1
      
b=2
      
a,b=b,a
      
print(b)
      
1
print(a)
      
2
>>> a=int(input())
...       
2
>>> b=int(input())
...       
3
>>> a,b=b,a
...       
>>> print(a)
...       
3
>>> print(b)
...       
2
>>> temp=a
...       
>>> a=b
...       
>>> b=temp
...       
>>> print(a)
...       
2
>>> print(b)
...       
3
>>> #arthimetc method to swap two numbers
...       
>>> a=10
...       
>>> b=12
...       
>>> a=a+b
...       
>>> b=a-b
...       
>>> a=a-b
...       
>>> 
>>> print("value of a",a)
...       
value of a 12
>>> print("value of b",b)
...       
value of b 10
=======
Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#upper()
#lower()
#captialize()
#title()
a="python course"
a.uper()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.uper()
AttributeError: 'str' object has no attribute 'uper'. Did you mean: 'upper'?
a.upper()
'PYTHON COURSE'
a="CODEGNAN"
a.lower()
'codegnan'
a="python course"
a.captialize()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
a.capitalize()
'Python course'
a.title()
'Python Course'

a="code"
a.isupper()
False
a.islower()
True
a.isalpha()
True
b="code gnan"
b.isalpha()
False
b="codegnan"
b.isalpha()
True
b=1234
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
b="1234"
b.isdigit()
True
a="rachitha123"
a.isalnum()
True
a="rac@123"
a.isalnum()
False

#split()
#join()
a="python java C C++"
a.split()
['python', 'java', 'C', 'C++']
b="i","am","learning"
"".join(b)
'iamlearning'
" ".join(b)
'i am learning'
#concatenation
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
print((a+" "+b).title())
Python Course
#formating
a=2
b=4
print("the sum of a and b is:",a+b)
the sum of a and b is: 6
#Dot Formating
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu
print("hello {}\nhello {}".format(a,b))
hello motu
hello patlu
#fstring

a="chota"
b="bheem"
print(f"hello {a}{b})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f"hello {a}{b}")
      
hello chotabheem
print(f"hello {a} {b}")
      
hello chota bheem
print(f"hello {a}hello{b}")
      
hello chotahellobheem
print((f"hello {a} hello{b}")).title()
      
hello chota hellobheem
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print((f"hello {a} hello{b}")).title()
AttributeError: 'NoneType' object has no attribute 'title'
print(f"hello {a}\nhello{b}")
      
hello chota
hellobheem
a=3
      
b=8
      
c=axb
      
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    c=axb
NameError: name 'axb' is not defined
c=a*b
      
a=4
      
b=5
      
print("product is {}{}".format(a*b))
      
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print("product is {}{}".format(a*b))
IndexError: Replacement index 1 out of range for positional args tuple
c=a*b
      
print("product is {}".format(c))
      
product is 20
print(f"product is{c}")
      
product is20
print(f"product is {c}")
      
product is 20

#Swapping of two variables
      
a=1
      
b=2
      
a,b=b,a
      
print(b)
      
1
print(a)
      
2
>>> a=int(input())
...       
2
>>> b=int(input())
...       
3
>>> a,b=b,a
...       
>>> print(a)
...       
3
>>> print(b)
...       
2
>>> temp=a
...       
>>> a=b
...       
>>> b=temp
...       
>>> print(a)
...       
2
>>> print(b)
...       
3
>>> #arthimetc method to swap two numbers
...       
>>> a=10
...       
>>> b=12
...       
>>> a=a+b
...       
>>> b=a-b
...       
>>> a=a-b
...       
>>> 
>>> print("value of a",a)
...       
value of a 12
>>> print("value of b",b)
...       
value of b 10
>>>>>>> d4f8f21c657bb527d926585f6f410478cea322ed
