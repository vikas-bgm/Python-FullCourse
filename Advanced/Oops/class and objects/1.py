class Student:
    #Attributes -->         Python objects can have attributes created dynamically,  so initilizesing is not reequired
    # roll_no = ""
    # name = ""
    # marks = ""
    # age = ""
    
    #Constructor
    def __init__(self, roll_no:int, name:str, marks:float, age:int) -> None:
        self.roll_no = roll_no
        self.name    = name
        self.marks   = marks
        self.age     = age       
    
    #Methods        
    def display(self):
        print(f"Roll No - {self.roll_no}")
        print(f"Name - {self.name}")
        print(f"Marks - {self.marks}")
        print(f"Age - {self.age}")        
        

student1 = Student(101, "Vikas", 100, 40)
student2 = Student(102,"Abc", 86, 35)
student1.display()
print("---------------")
student2.display()
