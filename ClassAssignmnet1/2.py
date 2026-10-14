#2]Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.
file = open("sample2.txt", "r")
lines = file.readlines()
print("Total number of lines:", len(lines))
print("Second line:", lines[1])
print("Fourth line:", lines[3])
file.close()