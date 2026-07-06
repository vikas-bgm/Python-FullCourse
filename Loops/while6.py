"""
Ask a number from the user, and count all the factors.

Enter a number = 10
4

Enter a number = 100
9
"""

num = int(input("Enter a number - "))
i = 1
count = 0

while i <= num:
    if num % i == 0:
        print(i, end =" ")
        count+= 1
    i+=1
print(f"\nTotal factors of {num} are {count}")