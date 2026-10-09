#Accept the number list from user and add 2 digit after 3rd postion in list then append a name then split the list and print the list
number_list = input("Enter a list of numbers separated by spaces: ").split()
number_list = [int(num) for num in number_list]  # Convert input strings to integers
# Add a 2-digit number after the 3rd position (index 2)
number_list.insert(3,8),(3,9)  # Example 2-digit number
# Append a name to the list
number_list.append("Python")

# Split the list into two parts: before and after the 3rd position
part1 = number_list[:3]  # Elements before the 3rd position
part2 = number_list[3:]  # Elements from the 3rd position onwards
print("Part 1:", part1)
print("Part 2:", part2)