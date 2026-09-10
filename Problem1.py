#write a program to check if the person in elgible for discount 

role=input("Enter your role: ")
age=int(input("Enter your age: "))
print ("Eligible for discount:",role=="student" and age<21)