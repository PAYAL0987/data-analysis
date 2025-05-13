#class Employee:
 #def __init__(self, name):
  #   self.name = name
   #  def show(self):
    #    print(f"The name is {self.name}"):
        
     
     
     #class Dancer:
      #   def __inti__(self, dance):
       #      self.dance = dance 
             
             
        #     class DancerEmployee(Employee, Dancer):
         #        def __init__(self, dance, name):
           #          self.dance = dance
          #           self.name = name 
                     
            #         o = DancerEmployee("Kathak "Shivani")
              #                      print(o.name)
             #                       print(o,dance)    
             
             # Parent class 1
class Father:
    def skills(self):
        print("Father: Gardening, Driving")

# Parent class 2
class Mother:
    def skills(self):
        print("Mother: Cooking, Art")

# Child class (inherits from both Father and Mother)
class Child(Father, Mother):
    def skills(self):
        # Calling both parent methods
        Father.skills(self)
        Mother.skills(self)
        print("Child: Python Programming")

# Create an object of Child
c = Child()
c.skills()