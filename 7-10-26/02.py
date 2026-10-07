# remove the items from the list 2nd and 5th location
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_2nd = numbers.pop(1)
remove_5th = numbers.pop(4)
print("numbers", numbers)

##
del numbers[0]
del numbers[5]
print("numbers after deleting 2nd and 5th elements:", numbers)
