#condinal statement
#if statement
no=int(input('enter the no='))
if no>0:
    print('no is big than zero')
else:
    print('no is small than zero')

print('outside of the block')
a=int(input('enter the value of a='))
b=int(input('enter the value of b='))
c=int(input('enter the value of c='))
if a>b and a>c:
    print('a is grater than b and c')
elif b>c:   
    print('b is big')

elif c>b:
    print('c is big')
else:
    print('all are equal')

