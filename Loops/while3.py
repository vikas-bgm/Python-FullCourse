# start to end print even numbers while loop

start = int(input("Enter a start number - "))
end = int(input("Enter an end number - "))

i = start

while i <= end:
    if i % 2 == 0:
        print(i)
    else:
        pass
    i+=1

        
        