minute = int(input("Enter a minute: "))
print("{minute}minutes is equal to {result}hours and {minutes}".format(minute=minute, result=minute//60, minutes=minute%60))