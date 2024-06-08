import random
import pygame
from matrix import Matrix


class Board:
    def __init__(self, arguments):
        pygame.init()

        self.width = arguments.get('width') or 1600
        self.height = arguments.get('height') or 800
        self.zoom = arguments.get('cell_size') or 4
        self.frame_rate = arguments.get('frame_rate') or 60
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.matrix = Matrix(int(self.width / self.zoom), int(self.height / self.zoom))
        self.display = pygame.display
        self.window = self.display.set_mode((self.width, self.height))


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
        self.clock.tick(self.frame_rate)