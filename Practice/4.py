# Ternary operation - single if statement example

age = int(input("Enter the age - "))

# if age >=18:
#     status = "Adult"
# else:
#     status = "Minor"

status = "Adult" if age >=18 else "Minor"

print(f"Your status is {status}")

