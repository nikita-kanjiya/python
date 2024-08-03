'''print('five types  of datatype in python  (1)number (2)string (3)touple (4)list (5)dictionary')
#list define by a [] braceses
li=[23,35,'nikita','kanjiya',90,'bca']
l2=['hello',53,'india','good morning',34,74,87,'hp','python']
print(li,l2)
print(type(li))
print(li[1:5])
print(li[1:])
print(li+l2)
print(l2[2:])
print(l2[3:8])
print('in a list you can change and update the index ')

#######


print('touple')
print('touple is read only, cannot chage like a static')
print('touple is defined in a simple braces like t=()')
tpl=(1,2,3,4,5,6,7,'touple',9,'python')
print(tpl)
print(tpl[2:])
print(tpl[2:9])
print(type(tpl))
print(tpl[0])
print(tpl[0:])

print('dictionary')
print('dictionary is a key value pair using ')
print('in dictionary {} is used')
d={
    "project":"Eventorganizer",
    "developed by":"Nikita & krishna",
    "databasetools":"php with mysql",
    "submitted by":"amit kaila & jignesh nayabpara"
}
print(d)
print(type(d))
print(d['project'])
print(d['developed by'])
print(d.keys())
print(d.values())'''

#operator in python

##  (1)Arithmetic operators


#c=int(input('enter  the value of c='))
'''
d=a+b+c
e=a-b-c
f=a*b*c
g=a/b
h=a//b
print(d,e,f,g,h)

#  (2)Assignment operators
a+=5
print(a)
a-=10
print(a)
a*=15
print(a)
a/=10
print(a)
a%=2
print(a)


#  (3)comparison operstor)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

#identity operator

print('is->return true if both variable are same object')
print('isnot ->return true if both variable are not same object')

a=int(input('enter the value of a='))
b=int(input('enter the value of b='))

print(a is b ," a and b is same")

print(a is not b ," a and b is not same")'''

#membership operator

kanjiya=['labhubhai','ramanikbhai','nitinbhai','punit','hardik']

print('labhubhai' in kanjiya)
print('nikita' in kanjiya)
print('nitinbhai' not in kanjiya)
print('kiran'  not in kanjiya)





