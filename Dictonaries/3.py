marks ={
    "science": 100,
    "maths": 85,
    "social": 89,
    "comps":96,
    }

total = 0
for sub in marks.keys():
    print(sub, marks[sub])
    total+= marks[sub]
print(f"Total marks = {total}")