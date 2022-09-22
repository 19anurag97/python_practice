#Problem Statement – Write a Python program to take two numbers from the user and print its sum.
def user_inputsum():
    x = int(input("Enter num 1"))
    y = int(input("Enter num 2"))
    sum = x + y
    print("sum is ", sum)

#user_input()
def type_conversion():
    x = 0.001
    y = 188
    z = 9j
    print(f'values: ',x,y,z)
    a = complex(x)
    b = float(y)
    c = complex(z)
    print(f'float->complex & int->float value after conversion',a,b,c)

type_conversion()

