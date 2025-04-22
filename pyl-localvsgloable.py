#x = 4
#print(x)

#def hello():
   # x = 5
    
    
   # print(f"The local x is {x}")
    #print("hello payal")
    
    #print(f"The global x is{x}")
    #hello()
   # x = 5
   # print(f"The globl x is {x}")
   
   
   
   x = 10 
   
   def my_function():
       global = x
       x = 4
       y = 5 # local variable
       print(y)
       
       my _function()
       print(x)
       #print(y) # this will cause an error y is a local varible and is not accessible of the function