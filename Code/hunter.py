# Hunter is derived from the Mobile_Simulton/Pulsator classes: i.e., it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model


class Hunter(Pulsator, Mobile_Simulton):
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self._width, self._height, 0, 5)
        self.randomize_angle()
        
    def update(self):
        Pulsator.update(self)
        self.move()
        self.wall_bounce()
        def p(arg):
            return isinstance(arg, Prey) and self.distance(arg.get_location()) <= 200
        eatable = model.find(p)
        if len(eatable) != 0:
            nearest = list(eatable)[0].get_location()
            for i in eatable:
                if self.distance(i.get_location()) < self.distance(nearest):
                    nearest = i.get_location()
            self.set_angle(atan2(nearest[1]-self._y, nearest[0]-self._x))
