#getter and setter traditional way

class Bank:
    def __init__(self, name:str, balance:float):
        self.name = name
        self.__balance = balance
    #Getter
    def get_balance(self):
        return self.__balance
    #Setter
    def set_balance(self,new_balance:float):
        self.__balance = new_balance

b1 = Bank("ABC",10000)
print(b1.get_balance())
b1.set_balance(2000)
print(b1.get_balance())