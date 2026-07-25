"""
 Reverse a list without using the .reverse() method or list slicing ([::-1]).
"""

def reverse_list(list1):
    n = len(list1)
    new_list1 = []
    for i in range(n-1, -1 , -1):
        new_list1.append(list1[i])
    return new_list1

list1 = [27, 17, 20, 100, 583, -17, 354, 0]
ans = reverse_list(list1)
print(ans)