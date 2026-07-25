with open("data1.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    
for line in lines:
    print(line.strip())