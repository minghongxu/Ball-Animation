# Runner
# A runner can escape from a predator in 50 pixels, including
# Blackhole, Pulsator and Hunter
from ball import Ball
from blackhole import Black_Hole
from math import atan2
import model


class Special(Ball):
    def __init__(self, x, y):
        Ball.__init__(self,x,y)
        self.randomize_angle()
        
    def update(self):
        Ball.update(self)
        def p(arg):
            return isinstance(arg, Black_Hole) and self.distance(arg.get_location()) <= 50
        dangerous = model.find(p)
        if len(dangerous) != 0:
            nearest = list(dangerous)[0].get_location()
            for i in dangerous:
                if self.distance(i.get_location()) < self.distance(nearest):
                    nearest = i.get_location()
            self.set_angle(atan2(self._y-nearest[1], self._x-nearest[0]))

    def display(self,canvas):
        canvas.create_oval(self._x-5, self._y-5,
                                self._x+5, self._y+5,
                                fill='pink')