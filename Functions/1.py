"""
Write a function that ask a number from user and prints if that
number is odd or even.
"""

def odd_even():
    num = int(input("Enter a number- "))
    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")
odd_even()