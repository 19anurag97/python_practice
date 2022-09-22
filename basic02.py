import sys

if len(sys.argv) != 3:
    raise ValueError("Enter Username and Password\n")

print(f' Your username is {sys.argv[1]} and your password is {sys.argv[2]}')

