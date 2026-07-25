try:
    
    with open("data1.txt", "r") as f:
        
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("File does not exists")
