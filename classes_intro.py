class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        pass
    
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2-x1)**2+(y2-y1)**2)**0.5
        
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

#  EXAMPLE OUTPUT

coordinate1 = (0,1)
coordinate2 = (1,0)

li = Line(coordinate1,coordinate2)

print("Distance" , li.distance())
print("Slope" , li.slope())


class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return 3.1415 * self.radius**2*self.height
    
    def surface_area(self):
        top = 2 * 3.1415 * self.radius**2
        return top + (2*3.1415*self.radius*self.height)

# EXAMPLE OUTPUT
c = Cylinder(2,3)

c.volume()

c.surface_area()