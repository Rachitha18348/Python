Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
print(type(d))
<class 'dict'>

d={'ram':12,'raju':23,'rachitha':65,'pooja':9}
print(d['ram'])
12
print(d['hi'])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(d['hi'])
KeyError: 'hi'

>>> print(d.get('raju'))
23
>>> print(d.get('hi'))
None
>>> d.update({'hello':44})
>>> d
{'ram': 12, 'raju': 23, 'rachitha': 65, 'pooja': 9, 'hello': 44}
>>> d.pop("ram")
12
>>> d
{'raju': 23, 'rachitha': 65, 'pooja': 9, 'hello': 44}
>>> d.popitem()
('hello', 44)
>>> d
{'raju': 23, 'rachitha': 65, 'pooja': 9}
>>> print(d.keys())
dict_keys(['raju', 'rachitha', 'pooja'])
>>> print(d.values())
dict_values([23, 65, 9])
>>> print(d.items())
dict_items([('raju', 23), ('rachitha', 65), ('pooja', 9)])
>>> d.setdefault('raju',54)
23
>>> d
{'raju': 23, 'rachitha': 65, 'pooja': 9}
>>> d.setdefault('lakh',54)
54
>>> d
{'raju': 23, 'rachitha': 65, 'pooja': 9, 'lakh': 54}
>>> d.update({'hello',44})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d.update({'hello',44})
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> d.setdefault('lakh':54)
SyntaxError: invalid syntax
>>> p=input()
raju
>>> d.pop(p)
23
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
