from settings import *
import pygame
import math


class Board:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        self.tile_size = TILESIZE
        self.width = math.sqrt(3) * self.tile_size
        self.height = 2 * self.tile_size

    # draws the board
    def draw(self):
        v = []
        rows = [3, 4, 5, 4, 3]
        self.screen.fill(BGCOLOUR)
        x = 200
        y = 150

        for row in range(5):
            x_offset = 0

            if row == 2:
                x_offset -= self.width / 2

            elif row % 2 == 0:
                x_offset = self.width / 2

            # loops x times for number of hexagons in row
            for i in range(rows[row]):
                x += self.width
                centre = (round(x + x_offset), round(y))  # stores centre of a hexagon in a tuple
                vertices = []

                # calculate vertices from centre of a hexagon
                for j in range(6):
                    angle_deg = 60 * j - 30
                    angle_rad = math.pi / 180 * angle_deg
                    pointx = centre[0] + self.tile_size * math.cos(angle_rad)
                    pointy = centre[1] + self.tile_size * math.sin(angle_rad)
                    vertices.append([math.floor(pointx), math.floor(pointy)])

                v.append(vertices)
                pygame.draw.polygon(self.screen, HEXCOLOUR, vertices)
                pygame.draw.circle(self.screen, BLACK, centre, 4, 4)

            y += self.height * 3/4  # offsets the y position after each row
            x -= self.width * rows[row]  # resets x back to starting position

        print(v)
