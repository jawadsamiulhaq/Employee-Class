class Employee():
    def getSalary(self):
        print(F"Salary Of Employee Working In {self.company} Is {self.salary}")
    def __init__(self,name,salary,company):
        self.name = name
        self.salary = salary 
        self.company = company 
        print("Employee Is Created")
    def getDetails(self):
        print(f"Name Of Employee Is {self.name}")
        print(f"Salary Of Employee Is {self.salary}")
        print(f"Company Of Employee Is {self.company}")

jawad = Employee("Jawad",50000,"Youtube")
jawad.getSalary()
jawad.getDetails()

