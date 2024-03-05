import pygame as pg
from settings import *
from math import *
from shapes import *

class Menu:
    def __init__(self, screen, width, height):
        
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
    
        self.screen = screen

        self.menu_surface = pg.Surface((width, height))
        self.menu_surface.fill('darkgray')

        self.cube = Cube(self.screen, 350)

        self.center = (self.menu_surface.get_size()[0] // 2, self.menu_surface.get_size()[1] // 2)

        self.sliders = [
            Slider((self.center[0], self.center[1] + 275), (100, 30), 1, 0.5, 100, "X"),
            Slider((self.center[0], self.center[1] + 225), (100, 30), 1, 0.5, 100, "Y"),
            Slider((self.center[0], self.center[1] + 175), (100, 30), 1, 0.5, 100, "Z"),
            Slider((self.center[0], self.center[1] + 125), (100, 30), 1, 0.5, 100, "Scale"),
        ]

        self.buttons = []
    
    def draw(self):

        self.cube.draw()
    
        mouse_pos = pg.mouse.get_pos()
        mouse = pg.mouse.get_pressed()
        self.screen.blit(self.menu_surface, (0, 0))

        for slider in self.sliders:
            if slider.container_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    slider.move_slider(mouse_pos[0])
            slider.render(self.screen)

        #for button in self.buttons:
        #    button.render(self.screen)
        #    if button.button_rect.collidepoint(mouse_pos):
        #        if mouse[0]:
        #            button.toggle(self.screen)
        
        self.cube.angle_x += radians(self.sliders[0].get_value()) * ROT_SPEED
        self.cube.angle_y += radians(self.sliders[1].get_value()) * ROT_SPEED
        self.cube.angle_z += radians(self.sliders[2].get_value()) * ROT_SPEED
        self.cube.scale = self.sliders[3].get_value() * SCALE
        
class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min_val: float, max_val: float, title: str):
        self.pos = pos
        self.size = size
        self.min_val = min_val
        self.max_val = max_val
        self.title = title

        self.font = pg.font.Font('freesansbold.ttf', 20)

        self.slider_left_pos = pos[0] - (size[0] // 2)
        self.slider_right_pos = pos[0] + (size[0] // 2)
        self.slider_top_pos = pos[1] - (size[1] // 2)

        self.initial_val = initial_val
        self.current_val = initial_val

        self.container_rect = pg.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pg.Rect((self.pos[0] // 2) + 10, self.slider_top_pos, 10, self.size[1])

    def move_slider(self, mouse_x):
        mouse_x = min(max(mouse_x, self.slider_left_pos), self.slider_right_pos)
        self.button_rect.centerx = mouse_x
        self.current_val = (mouse_x - self.slider_left_pos) / self.size[0] * (self.max_val - self.min_val) + self.min_val

    def render(self, screen):
        text = self.font.render(self.title, True, 'blue', 'white')
        pg.draw.rect(screen, "white", self.container_rect)
        screen.blit(text, self.container_rect)
        pg.draw.rect(screen, "darkblue", self.button_rect)

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return (button_val/val_range) * (self.max_val - self.min_val) + self.min_val

class Button:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, final_val: float, color: str, tog_col: str):
        self.pos = pos
        self.size = size
        self.init = initial_val
        self.final = final_val
        self.color = color
        self.ctog = tog_col

        self.button_left = self.pos[0] - (size[0 // 2])
        self.button_right = self.pos[0] + (size[0] // 2)
        self.button_top = self.pos[1] - (size[1] // 2)

        self.button_rect = pg.Rect(self.button_left, self.button_top, self.size[0], self.size[1])
        
        self.tog_rect = pg.Rect(self.button_left, self.button_top, self.size[0], self.size[1])

    def render(self, screen):
        pg.draw.rect(screen, self.color, self.button_rect)
    
    def toggle(self, screen):
        pg.draw.rect(screen, self.ctog, self.tog_rect)

class topMenu:
    def __init__(self, screen, pos: tuple, size: tuple, color):
        self.screen = screen
        self.color = color

        self.left = pos[0] - (size[0] // 2)
        self.top = pos[1] - (size[1] // 2)

        self.top_menu = pg.Rect(self.left, self.top)
    
    def render(self, screen):
        pg.draw.rect(screen, "white", self.top_menu)
    