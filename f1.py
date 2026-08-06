# File handling
#File handing is used to stored the data in a physical file for some audit purpiose 
#we can work with file handling in three different read, write, append mode 
file= open('data.txt','w')
file.write('first line \n')
file.write('second line \n')
file.write('third line \n')
file.close()
print("file created")

#create a file name student.txt and write student name address telephone no 


f=open("student.txt","w")
f.write('Name:Harry \n')
f.write("Address: Kathmandu \n")
f.write("Telephone No: 9851022347")
f.close()


