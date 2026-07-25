#Nested dictonaries

student = {
    "101" : {"name":"Rahul", "age":25, "city": "Bangalore"},
    "102" : {"name":"Raj", "age":24, "city": "Mumbai"},
    "103" : {"name":"Priya", "age":25, "city": "Pune"},
}
#how to access
#print(student)                      # Entire dict
#print(student["101"])               # {'name': 'Rahul', 'age': 25, 'city': 'Bangalore'}
print(student["103"]["city"])       # Pune

for roll_no , details in student.items():
    print(f" Roll No:{roll_no}, name = {details['name']}, age = {details['age']}")