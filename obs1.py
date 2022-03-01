from abc import ABC ,abstractclassmethod, abstractmethod
from turtle import shape
from multipledispatch import dispatch

class Shape(ABC):
    def __init__(self):
        self._area=0
        
    @abstractmethod
    def calArea(self):
        pass
    
    
    def showInfo(self):
        print()
        
 
#===================================================================================       

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
        
    def calArea(self):
        self._area=self.length*self.width
        
    @dispatch()
    def showInfo(self):
        print(f" Rectangle info: [{self._area}]")      
        

#===================================================================================

class Triangle(Shape):
    def __init__(self,base, height):
        self.base=base
        self.height=height
        
        
    def calArea(self):
        self._area=0.5*(self.base*self.height)
              
        
    def showInfo(self):
        print(f"Triangle info: {self._area}" )     
        

#===================================================================================        
class circle(Shape):
    def __init__(self, readius):
        self.radius=readius
        
        def calArea(self) :
            self._area=3.14*self.radius**2
            
        
        
        
t1=Triangle(5,8)
t1.calArea()
t1.showInfo()
               
        
        
        