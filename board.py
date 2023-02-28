from settings import *
import pygame
import math


class Board:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        self.tile_size = TILESIZE
        self.tiles = []

    # draws the board
    def draw(self):
        self.screen.fill(BGCOLOUR)
        posx = 306
        posy = 150
        rows = [3, 4, 5, 4, 3]
        v = []  # list of all vertices

        # loops through the row of hexagons (3 for 3 hexagons here)

        rows = [3, 4, 5, 4, 3]

        for o in range(5):

            x = rows[o]

            for i in range(x):
                vertices = []

                # loops through calculating the pos of vertices (6 as hexagon has 6 vertices)
                for j in range(6):
                    x = posx + self.tile_size * math.cos(math.pi / 2 + math.pi * 2 * j / 6)
                    y = posy + self.tile_size * math.sin(math.pi / 2 + math.pi * 2 * j / 6)
                    vertices.append([int(x), int(y)])

                self.tiles.append(vertices)
                v.append(vertices)
                posx += self.tile_size * math.sqrt(3)

            posy += self.tile_size * math.sqrt(3)

            if o == 1:
                posx = 306 - 86
            elif o % 2 == 0:
                posx = 306 - 43
            else:
                posx = 306

        print(v)

        # takes vertices array and uses values to draw each hexagon
        for vertices in self.tiles:
            pygame.draw.polygon(self.screen, HEXCOLOUR, vertices)

