# Raise exception

age = int(input("Enter age - "))
if age < 0:
    raise ValueError("Age cannot be negative")
if age > 150:
    raise ValueError("Enter realistic number")
print(f"Entered age is - {age}")