"""
Write a function called min_of_three that takes three numbers and returns
the smallest without using any built-in function.
"""

def min_no(n1,n2,n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    return n3
ans=min_no(10,14,12)
print(ans)