class Employee:
    def __init__(self, name, salary):
        self.name = Name 
        self.salary =salary
        
        @classmethod
        def fromStr(cls,String):
            return cls(string.split("-")[0], string.split("-")[1])
        
        e1 = Employee("Payal, 12000")
        print(e1.name)
        print(e1.salary) 
        
        String = "john-12000"
        e2 = Employee.fromStr(string)
        print(e2.name)
        print(e2.salary) 
        