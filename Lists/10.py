"""
Write a program that takes a list of numbers and, using a loop, determines
whether it is sorted in ascending order. Print True if it is sorted,
and False otherwise.
"""

def is_sorted(nums):
    n = len(nums)
    
    for num in range(0, n-1):
        if nums[num] > nums[num+1]:
            return False 
    return True
 
nums = [3, 6, 8, 9, 13, 17, 18, 23, 45, 58, 79, 100]
print(is_sorted(nums))
nums = [3, 6, 8, 9, 13, 17, 18, 23, 45, 15, 79, 100]
print(is_sorted(nums))