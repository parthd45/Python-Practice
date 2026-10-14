#4]Read a file, split its content into words, and store them in a list.
#Print the total number of words.
#Print all unique words.
with open("sample1.txt", "r") as file:
    content = file.read()
words = content.split()
print("Total number of words:", len(words))
unique_words = set(words)
print("Unique words:", unique_words)