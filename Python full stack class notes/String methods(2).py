Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="red is good"
print(a.startswith("r"))
True
print(a.startswith("red"))
True
print(a.index("red"))
0
print(a.find("e"))
1
print(a.rfind("o"))
9
print(a.count("o"))
2

#Modification Methods

x="you want to do practice"
print(x.repalce("you","I"))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(x.repalce("you","I"))
AttributeError: 'str' object has no attribute 'repalce'. Did you mean: 'replace'?
print(x.replace("you","I"))
I want to do practice
print(x.strip(" "))
you want to do practice
x="*********you want to do practice********"
print(x.lstrip("*"))
you want to do practice********
print(x.rstrip("*"))
*********you want to do practice
>>> 
>>> a="I am good girl"
>>> print(a.split())
['I', 'am', 'good', 'girl']
>>> b="1,2,3,4,5"
>>> print(b.split(","))
['1', '2', '3', '4', '5']
>>> a=[1,2,3,4]
>>> print(join(a))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(join(a))
NameError: name 'join' is not defined
>>> print(" ".join(a))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(" ".join(a))
TypeError: sequence item 0: expected str instance, int found
>>> a=['1','2','3','4']
>>> print(" ".join(a))
1 2 3 4
>>> 
>>> #advance formating - not that important
>>> 
>>> a="codegnan"
>>> print(a.zfill(20))
000000000000codegnan
>>> print(a.ljust(20,"&"))
codegnan&&&&&&&&&&&&
>>> print(a.rjust(20,"&"))
&&&&&&&&&&&&codegnan
>>> print(a.center(20,"&"))
&&&&&&codegnan&&&&&&
>>> print(a.center(19,"&"))
&&&&&&codegnan&&&&&
>>> print("I love {1} and {0}".format("Java", "python"))
I love python and Java
>>> name = "Charlie"
>>> age = 30
>>> print("My name is %s and I am %d years old." % (name, age))
My name is Charlie and I am 30 years old.
>>> name = "granny"
>>> marks = 90
>>> print(f"{name} scored {marks} marks in the exam.")
granny scored 90 marks in the exam.
