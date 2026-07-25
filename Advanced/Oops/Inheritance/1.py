# Inheritance structure

class Vehicle:
    def __init__(self, model:str) -> None:
        self.model = model
    
    def start(self):
        print(f"Starting...... {self.model}")
        

class Car(Vehicle):
    def drive(self):
        print(f"{self.model} is driving ....")

v1 = Vehicle("Maruti")
v1.start()
#v1.drive()                      # Will throw an error as drive() is not inside class Vehicle

c1 = Car("Swift")
c1.start()
c1.drive()