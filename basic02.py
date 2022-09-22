'''
Run this file by providing
command line arguments at command line

RUN:
# python basic02.py username passwd
'''
import sys
import random

if len(sys.argv) != 3:
    raise ValueError("Enter Username and Password\n")

print(f'Your username is {sys.argv[1]} and your password is {sys.argv[2]}')

print(f'Printig a random number\n',random.randrange(1, 10))

#strings as Arrays
a ="this string is an array of bytes.(or char of arrays)"
print(a[0])
print(a[1])
print(a[2]) 
print(a[3]) 
print(f'Length of string {len(a)}')

for i in "heyhlo":
    print(i)
