# dynamic for loop

start = int(input("Enter a start number - "))
end = int(input("Enter an end number -  "))
total=0

for i in range(start,end + 1):
    total+=i
    print(i)
print(f"Total sum of numbers = {total}")
