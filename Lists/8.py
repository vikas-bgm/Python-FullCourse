"""
Given a list of numbers, use a loop to calculate and print their average.
You can use len() to get the count of elements, but avoid using
sum() for the total.
"""

def avg_cal(lst):
    n = len(lst)
    total = 0
    for num in lst:
        total+=num
    return (total / n) 

lst = [6, -5, 4, 2, 10, 91, -75, 49, 9]
print(avg_cal(lst))