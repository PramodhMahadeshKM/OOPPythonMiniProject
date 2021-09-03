import re

f=open("sample.txt")
data=f.read()
key=input("enter the word to search: ")
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(regex.search(key) == None):
    if re.search(key,data):
        print(" Word found")
    else:
        print("word not found")
else:
    print("enter only alphanumeric values")

f.close()