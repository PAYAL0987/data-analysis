 class Vector:
     def __init__(self, i, j, k):
     self.i = i 
     self.j = j 
     self.k = k 
     
     def __str__(self):
         return f"{self.i}i + {self.j}j {self.k}k"
     
    
     v1 = Vector(3, 5, 6)
     print(v1)
      
      v2 =Vector(1, 2, 6)
      print(v2) 
      
      