# Looping in Lists

list1 = [1, 29, 17, 24, 35, 46, 78, 57]

#while loop example

i = 0
n = len(list1)
count = 0

while i <= n - 1:
    if list1[i] % 2 != 0:
        count+=1
    i+=1
print(f"Total count of Odd numbers is - {count}")
    