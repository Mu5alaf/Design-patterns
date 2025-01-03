class DrawingAPIOne(object):
    """implementation specific abstraction:concrete class one"""
    
    def draw_circle(self,x,y,radius):
        print("api 1 drawing a circle at ({}, {} with radius {} !)".format(x,y,radius))
        
class DrawingApuTwo(object):
    """implementation specific abstraction: concrete class two"""
    def draw_circle(self,x,y,radius):
        print("api 2 drawing a circle at ({}, {} with radius {} !)".format(x,y,radius))

    

class Circle(object):
    
    """implemnetation independent abstraction"""
    def __init__(self,x,y,radius,drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api
        
    def draw(self):
        self._drawing_api.draw_circle(
            self._x,
            self._y,
            self._radius,
        )
        
    def scale(self, percent):
        self._radius *= percent

circle1 = Circle(1,2,3,DrawingAPIOne())

circle1.draw()


circle2 = Circle(2,4,5,DrawingApuTwo())

circle2.draw()

