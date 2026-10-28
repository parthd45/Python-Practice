#Accept the name and check if its palindrome or not
name = input("Enter your name: ")
if name == name[::-1]: ##check if the name is equal to its reverse
    print(name +"is a palindrome.")
else:
    print(name +"is not a palindrome.")