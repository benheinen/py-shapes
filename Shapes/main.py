'''
Create a Custom UI that allows user to change:
    - X rotation
    - Y rotation
    - Z rotation
    - Scale
    - Has sliders 

    - Display current slider values in top right corner

    - Have a movable camera 
'''

import pygame as pg
import sys
from settings import *
from gui import *
from shapes import *

class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.menu = Menu(self.screen, 100, HEIGHT)
    
    def draw(self):
        self.screen.fill('black')
        self.menu.draw()
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.draw()
    
if __name__ == '__main__':
    app = App()
    app.run()
