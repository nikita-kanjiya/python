#loop
'''

no=int(input('enter the no='))

while no<11:
    print(no)
    no+=1
else:
    print('out of while blog')

for i in 'Nikita':
    print(i) 

brosis=['Nikita','Kiran','Punit','Ankita','Hardik']
for n in brosis:
    print(n)



for i in reversed(range(1,100)):
    print(i)

for i in range(0,100):
    if i==12:
        pass
        print('in the block ')
        
a=min(1,5,4,36,36,657,5,54) 
print(a)

b=max(1,5,4,36,36,657,5,54) 
print(b)

c=abs(-54) 
print(c) 

d=pow(5,4) 
print(d)'''

import math

e=math.sqrt(43)
print(e)

f=math.ceil(-43.09)
print(f)

g=math.floor(-43.09)
print(g)

print(math.pi)


import random

print(random.randrange(1,100))

rosis=['Nikita','Kiran','Punit','Ankita','Hardik']
print(random.choice(rosis))

str='kanjiya nikita'
print(random.choice(str))

print('HellO WOrld'.lower)
print('HellO WOrld'.upper)
print('HellO WOrld'.title())
print('HellO WOrld'.find('H'))
n='swagatam indida shubh din'
r=n.replace('india','bharat')
print(n)
print(r)
k='good morning india we have a good day'
print(k.islower)
print(k.capitalize())
print(k.isupper)
#print(k.alpha)

str1=['a','b','c','d','e','f']
h='*'.join(str1)
print(h)
print(str1)





