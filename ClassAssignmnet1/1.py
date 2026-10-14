#1]Write a program to read a file and count how many vowels are present in its content.
f =open("sample1.txt","r")
data =f.read()
count = 0
for ch in data.lower():
    if ch in "aeiou":
        count += 1
print("Number of vowels in the file:", count)
f.close()