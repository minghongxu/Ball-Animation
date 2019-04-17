# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey): 
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,0,5)
        self.randomize_angle()
        
    def update(self):
        if random.random() < 0.3:
            self._speed += random.uniform(-0.5,0.5)
            while self._speed < 3 or self._speed > 7:
                self._speed += random.uniform(-0.5,0.5)
            self._angle += random.uniform(-0.5,0.5)
        self.move()
        self.wall_bounce()

    def display(self,canvas):
        canvas.create_oval(self._x-5, self._y-5,
                                self._x+5, self._y+5,
                                fill='yellow')
