marks = {
    "science": 100,
    "maths": 85,
    "social": 89,
    "comps": 96,
}

inp = input("Enter subject to be searched - ")

if inp in marks:
    print(f"Subject {inp} Found")
    print(marks[inp])
else:
    print("Subject not found")