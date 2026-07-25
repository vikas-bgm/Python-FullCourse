marks ={
    "science": 100,
    "maths": 85,
    "social": 89,
    "comps":96,
    }
inp = input("Enter key - ")
if inp in marks:
    print(marks[inp])
else:
    print("Key does not exist")

