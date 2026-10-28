#1]Write a program to read a file and count how many vowels are present in its content.
f=open("sample.txt","r")
file=f.read()
count=0
for ch in file.lower():
    if ch in "aeiou":
        count+=1
print(count)
f.close()          