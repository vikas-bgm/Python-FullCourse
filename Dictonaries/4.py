marks ={
    "science": 100,
    "maths": 85,
    "social": 89,
    "comps":96,
    }

total = 0
for subject, mark in marks.items():
    print(f"Subject : {subject}, Marks : {mark}")
    total+= mark
print(f"Total = {total}")
    