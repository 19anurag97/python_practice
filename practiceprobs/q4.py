'''
Write a Python program which accepts a sequence of comma-separated 
numbers from user and generate a list and a tuple with those numbers.
'''
vars = input("enter some / separated values.    ")
li = vars.split("/")
tup = tuple(li)
print(li)
print(tup)

'''
Write a Python program to accept a filename
from the user and print the extension of that.

'''
filename = input("Enter the filename:   ")
a1 = filename.rsplit('.')
print(a1[1])

'''
Write a Python program to display the examination schedule. 
(extract the date from exam_st_date).
exam_st_date=(11,12,2022)
'''
exam_st_date=(11,12,2022)
print("Exam date is %i/%i/%i"%exam_st_date)

"""
Write a Python program that accepts an integer (n) and computes the value 
of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
5 55 555
"""
a = int(5)
#sum1 = n + (n**2) + (n**3)
#sum2 = n + (n*10+5) + (n*100+55)
n1 = int ("%s" % a)
n2 = int ("%s%s" % (a,a))
n3 = int ("%s%s%s" % (a,a,a))
print (n1+n2+n3)

