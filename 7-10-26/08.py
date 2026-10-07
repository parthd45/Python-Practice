#Accept the senntence and count the vowels in it
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in sentence if char in vowels)
print("Number of vowels in the sentence:", vowel_count)