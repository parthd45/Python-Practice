class InvalidAgeError(Exception):
    pass



try:
    age = 15
    if age < 18:
        raise InvalidAgeError("You must be 18 or older")
    print("Eligible")
except InvalidAgeError as e:
    print("Error:", e)
finally:
    print("Program completed")