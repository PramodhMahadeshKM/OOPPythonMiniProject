import re

file = open('email.txt', 'r')
total_list = []
for line in file:
    k = line.rstrip()
    total_list.append(k)
size = len(total_list)
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
for i in range(0,size):
    if(re.search(regex,total_list[i])):   
        print("Valid Email")   
    else:   
        print("Invalid Email")

file.close()