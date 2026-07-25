class Bank:
    def __init__(self, name:str, balance:float) -> None:
        self.name = name
        self.__balance = balance            # Private attribute
    
    def deposit(self, amount:float):
        if amount < 0:
            print("Invalid Amount")
        else:
            self.__balance+= amount 
    
    def get_balance(self):
        return self.__balance
        
b1 = Bank("ABC", 2000)

print(b1.get_balance())
b1.deposit(5000)
b1.__balance = 1000
print(b1.get_balance())