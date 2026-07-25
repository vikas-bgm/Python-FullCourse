

def addition (a:int, b:int) ->int:
    return a + b

def subtraction (a:int, b:int) ->int:
    return a - b

def multiplication (a:int, b:int) ->int:
    return a * b

def division (a:int, b:int) ->float:
    return a / b

PI = 3.14       # For constants values we use capital letter

if __name__ == "__main__":
    
    print(f"Calculator filename __name__ = {__name__}")     # in current file this will be main
    print("Testing this code - START")
    result = addition(10,20)
    print(f"Result is = {result}")
    print("Testing this code - END")