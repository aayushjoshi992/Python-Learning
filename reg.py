import re
# str='''Rohit is 33 years old and Dipika is 11 yrs old Chandan is 43 years old, Gautam is 5 years old , Ram is 1115yrs old'''
# ages=re.findall(r'\d{1,3}',str)
# print(ages)

# names=re.findall(r'[A-Z][a-z]*',str)
# print(names)


# nameAgeDict={}
# x=0
# for name in names:
#     nameAgeDict[name]=ages[x]
#     x=x+1

# print(nameAgeDict)

# mobile no val

# mob=input("Enter you mobile number: ")
# reg=re.fullmatch('[7-9][0-9]{9}',mob)
# if reg!=None:
#     print("Valid mob no: ",mob)
# else:
#     print("Invalid mob no format")


#email validation
regx=r'\b[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[a-zA-Z0-9-.]+$'
email='rakesh_abc.9+@gmail.com'
print(re.match(regx,email))
if re.match(regx,email):
    print("Valid Email")
else:
    print("Invalid Email")



