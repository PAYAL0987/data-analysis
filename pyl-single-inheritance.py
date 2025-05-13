#def Animal: 
    #def __init__(self, name, species):
        #self.name = name 
        #self.species = species 
        
        #def make_sound(slef):
          #  print("Sound made by the animal") 
            
           # def make(Animal):
            #    def __init__(self, name,breed);
             #   Animal.__init__(self, name, sepies="Dog")
              #  self.breed = breed 
                
               # def make_sound(self):
                #    print("Bark!")
                    
                    
                 #   d = dog("Dog" "Doggerman")
                  #  d.make_sound()
                    
                   # a = Animal("dog", "Dog")
                   # a.make_sound() 
                   
                   # Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating an instance of Dog
d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog