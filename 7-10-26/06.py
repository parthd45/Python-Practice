#Accept two values S and N. print the square of first N numbers starting from S
S = int(input("Enter the starting number S: "))
N = int(input("Enter the number of terms N: "))

for i in range(S, S + N):
    print(i ** 2)