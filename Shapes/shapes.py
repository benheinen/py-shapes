import pygame as pg
import numpy as np
from math import *
from settings import *

class Cube:
    def __init__(self, screen, offset):
        self.screen = screen
        self.offset = offset

        self.scale = SCALE

        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0 

        self.proj_matrix = [
            [1, 0, 0,],
            [0, 1, 0],
            [0, 0, 0],
        ]

        self.points = [n for n in range(8)]
        self.points[0] = [[-1], [-1], [1]]
        self.points[1] = [[1],[-1],[1]]
        self.points[2] = [[1],[1],[1]]
        self.points[3] = [[-1],[1],[1]]
        self.points[4] = [[-1],[-1],[-1]]
        self.points[5] = [[1],[-1],[-1]]
        self.points[6] = [[1],[1],[-1]]
        self.points[7] = [[-1],[1],[-1]]
    
    def mult_matrix(self, a, b):
        a_rows = len(a)
        a_cols = len(a[0])

        b_rows = len(b)
        b_cols = len(b[0])

        product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

        if a_cols == b_rows:
            for i in range(a_rows):
                for j in range(b_cols):
                    for k in range(b_rows):
                        product[i][j] += a[i][k] * b[k][j]

        return product
    
    def connect_points(self, i, j, points):
        pg.draw.line(self.screen, "white", (points[i][0], points[i][1]) , (points[j][0], points[j][1]))

    def draw(self):
    
        rotation_x = [[1, 0, 0],
            [0, cos(self.angle_x), -sin(self.angle_x)],
            [0, sin(self.angle_x), cos(self.angle_x)]]

        rotation_y = [[cos(self.angle_y), 0, sin(self.angle_y)],
                        [0, 1, 0],
                        [-sin(self.angle_y), 0, cos(self.angle_y)]]

        rotation_z = [[cos(self.angle_z), -sin(self.angle_z), 0],
                        [sin(self.angle_z), cos(self.angle_z), 0],
                        [0, 0, 1]]
        points = [0 for _ in range(len(self.points))]

        i = 0

        for point in self.points:
            rotate_x = self.mult_matrix(rotation_x, point)
            rotate_y = self.mult_matrix(rotation_y, rotate_x)
            rotate_z = self.mult_matrix(rotation_z, rotate_y)
            point_2d = self.mult_matrix(self.proj_matrix, rotate_z)

            x = (point_2d[0][0] * self.scale) + self.offset
            y = (point_2d[1][0] * self.scale) + self.offset

            points[i] = (x,y)
            i += 1
            pg.draw.circle(self.screen, "red", (x,y), 5)
        
        self.connect_points(0, 1, points)
        self.connect_points(0, 3, points)
        self.connect_points(0, 4, points)
        self.connect_points(1, 2, points)
        self.connect_points(1, 5, points)
        self.connect_points(2, 6, points)
        self.connect_points(2, 3, points)
        self.connect_points(3, 7, points)
        self.connect_points(4, 5, points)
        self.connect_points(4, 7, points)
        self.connect_points(6, 5, points)
        self.connect_points(6, 7, points)