#2]Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.
f=open("sample.txt","r")
file=f.readlines()
print(len(file))
print(file[1])
print(file[3])
f.close()