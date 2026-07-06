"""
Write a function called find_max that takes three numbers as
parameters and prints the largest one.
"""

def find_max(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print(f"Largest number - {n1}")
    elif n2 > n1 and n2 > n3:
        print("Largetst number - ",n2)
    else:
        print("Largetst number - ",n3)

find_max(10,20,23)