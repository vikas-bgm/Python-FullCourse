"""
 Given a list, remove all duplicate elements while preserving the original
order of the unique items.
"""

def duplicate_remove(list1):
    new_list = []
    for num in list1:
        if num not in new_list:
            new_list.append(num)
    return new_list

list1 = [1, 3, 4, 1, 3, 100, 45, 1, 45, 4, 19, 10, 3 , 10]
print(duplicate_remove(list1))