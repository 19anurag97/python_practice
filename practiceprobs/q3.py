from math import pi
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print ("Enter radius of circle")
r = float(input("Input radius of circle"))
area = float(pi * r**2)
print(f'"Area of circle is: {area}"') 
print (area)
first_name=input("Your first name: ")
last_name=input("Last name:")
print(f'{last_name} {first_name}')

