"""
Given a list of numbers, write Python code using a loop to find and print the
largest element. Do not use the built-in max() function.
"""

nums = [26, 55, 64, 32, 10, 91, 75, 149, 19]

maxi = 0

for num in nums:
    if num > maxi:
        maxi = num
print("The Largest number is - ", maxi)

