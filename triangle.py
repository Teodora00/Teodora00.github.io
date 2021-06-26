import math

class Triangle:
    def __init__(self,a,b,c):
        self.length_a = a
        self.length_b = b
        self.length_c = c
        
    def tiangle_perimiter(self):
     perimiter = self.length_a + self.length_b + self.length_c
     return print(perimiter)

    def triangle_area(self, h):
         s = (self.length_a + self.length_b + self.length_c) // 2
         area = math.sqrt(s *( s - self.length_a ) * ( s - self.length_b ) * ( s - self.length_c ))
         return print(area)

    def triangle_scale(self, scale_factor):
        return Triangle(scale_factor * self.length_a, scale_factor + self.length_b, scale_factor * self.length_c)
 

    def is_valid(self):
        if self.length_a + self.length_b > self.length_c:
            return True
        elif self.length_a + self.length_c > self.length_b:    
            return True
        elif self.length_b + self.length_c > self.length_a: 
            return True
        else:
            return False    

    def is_right(self):
        a = math.pow(self.length_a,2)
        b = math.pow(self.length_b,2)
        c = math.pow(self.length_c,2)
        if max(a, b, c) == (a + b + c - max(a, b, c)):
            return True 
        else:
            return False    
