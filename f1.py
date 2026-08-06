# File handling
#File handing is used to stored the data in a physical file for some audit purpiose 
#we can work with file handling in three different read, write, append mode 
file= open('data.txt','w')
file.write('first line \n')
file.write('second line \n')
file.write('third line \n')
file.close()
print("file created")

with open('abc.txt','w') as f:
    f.write("abc")
print("file created")

