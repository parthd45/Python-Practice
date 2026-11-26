age =15
try:
    if age<18:
        raise ValueError("Age must be 18 ")
    print("Eligible")
except ValueError as e:
    print("Error:",e)
print("Program Completed")    