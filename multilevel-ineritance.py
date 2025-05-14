#class Animal:
 #   def __init__(self, name, species)
  #  self.name = Name 
   # self.species = species 
    
    #def show_details(self):
     #   print(f"Name: {self.name}")
      #  print(f"Species: {self.sepcies}") 
        
       # class dod(Animal):  
           #def __inti__(self, name, breed):
             #   Animal.__init__(self, name, sepcies="dog")
            #    self.breed = breed 
                
              #  class GoldenRetiever(Dog):
               #     def __init__(self, name, breed="Goldenever")
                #    self.color = color
                    
                    
                    
                 #   def show_details(self):
                  #      dog.show_details(self)
                   #     print(f"colo GoldRetriver")
                    #    self.color = color
                        
                     #  def show_details(self):
                      #      Dog.show_details(self)
                       #     print(f"Color: {self.color}")
                            
                        #    o = GoldenRetiever("tommy," "Black")
                         #   o.show_details()
                         
                         # Base class
#class Animal:
  #  def sound(self):
 #       print("Animals make sounds")

# Derived class 1
#class Dog(Animal):
 #   def bark(self):
#        print("Dog barks")

# Derived class 2
#class Cat(Animal):
 #   def meow(self):
        #print("Cat meows")

# Using the classes
#d = Dog()
#d.sound()
#d.bark()

#c = Cat()
#c.sound()
#c.meow()


# Base class
class Animal:
    def move(self):
        print("Animals can move")

# Derived class 1 (single inheritance from Animal)
class Mammal(Animal):
    def feed_milk(self):
        print("Mammals feed milk")

# Derived class 2 (inherits from Animal)
class Bird(Animal):
    def fly(self):
        print("Birds can fly")

# Derived class 3 (inherits from both Mammal and Bird - multiple inheritance)
class Bat(Mammal, Bird):
    def echo(self):
        print("Bats use echolocation")

# Using the class
b = Bat()
b.move()       # From Animal
b.feed_milk()  # From Mammal
b.fly()        # From Bird
b.echo()       # From Bat