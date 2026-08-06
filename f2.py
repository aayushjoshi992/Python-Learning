# rf=open("data.txt","r")
# print(rf.read())
# rf.close()

# rf=open('data.txt','r')
# lines=rf.readlines()
#  print(lines)
# word="first"
# i=1
# for line in lines:
#     print(i,line.strip())
#     i=i+1
#     if word in line:
#         print("match found")
#     else:
#         print("match not found")


lines=["Python is easy","I am learning Java", "PYTHON is powerful" ]
word='python'
for line in lines:
    if word.lower() in line.lower():
        print("match found", word)
    else:
        print("match not found")


