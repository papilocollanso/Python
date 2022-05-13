# Python has functions for creating, reading, upding and deleting files

# Open a file



myFile = open('myfile.txt','w')

#Get some info 

"""print('Name: ', myFile.name)
print('is Closed ', myFile.closed)
print('Opening Mode: ', myFile.mode)"""

#write to file

myFile.write('i love python')
myFile.write(' and javasScript ')
myFile.close()
print('is Closed ', myFile.closed)

#Append to file
myFile =open('myfile.txt','a')
myFile.write('i also like Mathematics')
myFile.close()

#read from file
myFile =open('myfile.txt','r+')
text = myFile.read(10)
print(text)
