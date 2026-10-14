sentance=input("Enter a sentance:")
words= sentance.split()
longest=max(words,key=len)
print("The longest word is:",longest)