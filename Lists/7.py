"""
Write a program that takes a list and a target number. Use a loop to determine if
the target number exists in the list. Do not use the in operator.
"""

def does_target_exist(lst, target):
    for num in lst:
        if num == target:
            return True 
    return False 

nums = [1,3,5,6,8,42,100]
print(does_target_exist(nums,42))
print(does_target_exist(nums, 9))
print(does_target_exist(nums, 100))