"""BASICS:
Practice on strings in Python
"""
txt = "hey, this is a string.You need to find a word inside it."
check = print("thisis" in txt)

def findstring():
    if check == True:
        print("yes string exists")    
    else:
        print("string not present")

def findstring01():
    if "find a word" not in txt:
        print("Yes string is present in txt")

def slicetxt():
    print(txt[:6])#0 is the index.
    print(txt[-9:-3])#nside

def replace_string():
    print(txt.replace("find", "replace"))
    print(txt.replace("hey,", "yes"))

findstring()
findstring01()
slicetxt()
replace_string()