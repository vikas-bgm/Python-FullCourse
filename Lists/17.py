"""
 Given a list of numbers (which may contain duplicates), write a Python script
that takes an integer as input from the user and removes all occurrences of that
integer from the list.
"""

def duplicate(list1, target):
    new_list =[]
    for num in list1:
        if num != target:
            new_list.append(num)
    return new_list

list1 = [1, 1, 1,2,1,3,2,1,56,188,56,100,87,17,3,33]
print(duplicate(list1, 1))

