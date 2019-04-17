# Black_Hole is derived from Simulton: i.e., it updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)

    def contains(self, prey):
        r = self.get_dimension()[0]/2
        loc = prey.get_location()
        return self.distance(loc) <= r
        
    def update(self):
        eaten = set()
        def p(arg):
            return isinstance(arg, Prey) and self.contains(arg)
        eatable = model.find(p)
        for i in eatable:
            model.remove(i)
            eaten.add(i)
        return eaten

    def display(self,canvas):
        r = self.get_dimension()[0]/2
        canvas.create_oval(self._x-r, self._y-r,
                                self._x+r, self._y+r,
                                fill='black')
    
