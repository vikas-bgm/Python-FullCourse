"""
Q8: Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."
"""

num1 = int(input("Enter number 1 - "))
num2 = int(input("Enter number 2 - "))

if num1 > num2:
    print(f"{num1} is greater then {num2}")
elif num2 > num1:
        print(f"{num2} is greater than {num1}")
else:
    print(f" {num1} equals {num2}")