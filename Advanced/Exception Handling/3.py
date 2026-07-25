try:
    num1 = int(input("Enter number 1 - "))
    num2 = int(input("Enter number 2 - "))

    print(f"num1/num2 = {num1/num2}")
except Exception as e:
    print(f"Exception Type : {type(e).__name__}")
    print(f"Error message : {e}")