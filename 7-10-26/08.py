#Accept the senntence and count the vowels in it
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count=0
for name in sentence:
    if name in vowels:
        count+=1     
print("Number of vowels in the sentenvowel_",count)