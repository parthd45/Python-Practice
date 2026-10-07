#1
Print ="  Wellcome to the world of Python programming!  "
print("Remove spaces", Print.strip())

#2
text = Print.strip()
print("capitalize First letter of the string:", text.capitalize())

#3
print("Convert to uppercase:", text.upper())

#4
print("text in lowercase:", text.lower())

#5
print(text.title())

#6
print("letter o occurs:", text.count("o"), "times in text")

#7
print("position of Python in text:", text.find("Python"))

#8
print("text after replacement:", text.replace("Python", "Java"))

#9
print(text.startswith("Wellcome"))
print(text.endswith("programming!"))

#10
print("simple split of text:", text.split(" "))

#11
print("count the vowels in text:", text.count("a") + text.count("e") + text.count("i")
       + text.count("o") + text.count("u"))

#12
text1 = "Ha "
print(text1*3)

text2 = "Nayan"
print("accentuate text2:", text2)

print("replace 'a' with 'A':", text2.replace("a", "A"))


print("count of 'a' in text2:", text2.count("a"))

print("sort the text2:", sorted(text2))

#empty list
my_list = []
print(my_list)

#With List
my_list= ["1", "2", "3"]
print(my_list[0])
print(my_list)


colour = ["red", "green", "blue"]
colour.append("yellow")
print(colour[0])

last_colour = colour.pop()
print(last_colour)
print("after colour.pop():", colour)


##
number = [1, 2, 3, 4, 5]
print("List in ascending order:", sorted(number))
print("List in descending order:", sorted(number, reverse=True))

#create a list of 10 numbers and display the sum of last 4 elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_last_4 = sum(numbers[-4:])
print("Sum of last 4 elements:", sum_last_4)

# remove the items from the list 2nd and 5th location
#print the difference between the largest and smallest number in the list
#append a new element to a list which is half of the item of 3rd position in the list


