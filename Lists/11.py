"""
 Find the largest and smallest number in a list without using built-in functions
like max() or min().
"""

list1 = [10,25,8,187,-1,0,35,75,204,199,-127, 1005, -345]

maxi = list1[0]
mini = list1[0]
for num in list1:
    if num > maxi:
        maxi = num
    if num < mini:
        mini = num

print(f"Largest number in list is - {maxi}")
print(f"Smallest number in list is - {mini}")