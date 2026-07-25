try:
    age = int(input("Enter age - "))

    if age >= 18:
        print("Adult")
    else:
        print("Minor")
except:
    print("Some error")
print("Done")