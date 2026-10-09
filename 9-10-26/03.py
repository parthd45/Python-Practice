#Accept the name and check if its palindrome or not
name = input("Enter your name: ")
if name == name[::-1]:
    print(f"{name} is a palindrome.")
else:
    print(f"{name} is not a palindrome.")