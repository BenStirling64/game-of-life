import random
import pygame
from matrix import Matrix


class Board:
    def __init__(self, width=1600, height=800, zoom=4):
        pygame.init()

        self.width = width
        self.height = height
        self.zoom = zoom
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.matrix = Matrix(int(width / zoom), int(height / zoom))
        self.display = pygame.display
        self.window = self.display.set_mode((width, height))


    def tick(self):
        # inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        # drawing
        self.window.fill('black')

        for coords in self.matrix.cells:
            pygame.draw.rect(self.window, pygame.Color('white'), pygame.Rect(coords[0] * self.zoom, coords[1] * self.zoom, self.zoom, self.zoom))

        pygame.display.flip()

        # logic update
        self.matrix.update()

        # clock ticking
        self.clock.tick(60)