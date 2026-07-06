# Sum of all the numbers from 1 to 100.

start = int(input("Enter a start number - "))
end = int(input("Enter an end number - "))

i = start
total =0

while i <= end:
    total = total + i 
    i+=1
print(f"Toatl= {total}")