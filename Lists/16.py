"""
 Create a list containing the squares of numbers from
1 to 10 (i.e., [1, 4, 9, ..., 100]).
"""

def square_nums(list1):
    new_list = []
    for num in list1:
        new_list.append( num * num)
    return new_list

list1 = [1,2,3,4,5,6]
print(square_nums(list1))