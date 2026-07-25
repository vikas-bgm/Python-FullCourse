try:
    num1 = int(input("Enter number 1 - "))
    num2 = int(input("Enter number 2 - "))

    print(f"num1/num2 = {num1/num2}")
except ZeroDivisionError:
    print("Cannot divide a number by 0, please enter correct number")
except ValueError:
    print("Please enter integer ")
except:
    print("Some error occured")

