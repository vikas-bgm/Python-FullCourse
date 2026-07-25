"""
 Given two lists, merge them into a single new list without modifying the originals.
"""

# def merge_lists(list1, list2):
#     return list1 + list2

# list1 = [1,2,3]
# list2 = [3,5,7]
# print(merge_lists(list1,list2))

def merge_lists(list1, list2):
    new_list1 = []
    for num in list1:
        new_list1.append(num)
    for num in list2:
        new_list1.append(num)
    return new_list1

list1 = [1,2,3]
list2 = [3,5,7]
print(merge_lists(list1,list2))