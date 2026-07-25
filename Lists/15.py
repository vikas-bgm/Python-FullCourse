"""
 Separate a list of integers into two distinct lists: one containing all the
even numbers and the other containing all the odd numbers.
"""

def even_odd_list(list1):
    even_list = []
    odd_list = []
    for num in list1:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    print(f"Even list - {even_list}")
    print(f"Odd list - {odd_list}")

list1 = [1,0,34,28, 107, 111, 36, 500, 23]
even_odd_list(list1)