print("This is the pgm of division calculator")
print("Pogram starting")
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("Program Executed Succefffuly ")    
finally:
    print("This block genrate everytime ")    