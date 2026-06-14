


l=['a','b','c','d','e']
for i in l:
    print(i.upper())



l=['a','b','c','d','e']
for index,char in enumerate(l):
    print(f"{index} {l.upper()}")

l=['a','b','c','d']
r=len(l)
for i in range(r-1,-1,-1):
     print(i,r[i].upper())








l=['mani','PANITHA','nanDINI','rAM']
r=len(l)
for i in range(r):
     if i%2==0:
        print(l[i].upper())
    else:
       print(l[i].lower())


