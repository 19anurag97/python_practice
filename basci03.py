'''
x = 5
X = 910
y = "anurag"
Y = "bisht"
z = 310.01
'''

#assign multiple values at a time:
x, y, z, X, Y = 5, "anurag", 310.01, 910, "bisht"

print(int(x))
print(str(y))
print(str(z))#float->str, str->float,//310.0

#know the type of vars using type()
print(type(x))
print(type(y))
print(type(z))#we are not changing float value,when we did str(z).

print(int(X))
print(str(Y))

#output multiple variables at a time.
print(x, y, z, X, Y)

#concat strings add spaces and newline
print(y + ' ' + Y + '\n')

def localvar_func():#local vars with same name as global vars, 
    x, y, z = 9, "Mark", 310.02
    print(f'same name variables inside a functon are:\n',x,y,z)

localvar_func()
print(f'Global variables are:',x,y,z)#no change will happen in global variable.

def globalvar_func():#create global var inside a function using Keyword global.
    print('create a global var inside a function\n')
    global q 
    q = "heyiamaglobalvariable"

def access_global():#access global var inside a function created inside another function.
    A = q
    print(f'Global variable declared inside funct() is:\n',A)

globalvar_func()

print(f'Global variable declared inside funct() & accessible outside function are:\n',q)

access_global()

#assign single value to multiple vars:
ax = ay = az = "samevalue"
print(ax,ay,az)


