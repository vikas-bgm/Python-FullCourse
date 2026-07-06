# Nested if statements

age = int(input("Enter age - "))
certificate = True

if age >= 18:
    if certificate is True:
        print("You will be hired")
    else:
        print("You cannot be hired as no certificate")
else:
    print("Age is less than 18")