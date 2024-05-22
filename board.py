import random
import pygame
import life_structure
import matrix


class Board:
    def __init__(self, width, height, zoom):
        pygame.init()

        self.width = width
        self.height = height
        self.zoom = zoom
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.structure = life_structure.LifeStructure(matrix.NFTMatrix(int(width / zoom), int(height / zoom)))
        self.display = pygame.display
        self.window = self.display.set_mode((width, height))


    def tick(self):
        # inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        # drawing
        self.window.fill('black')

        for coords in self.structure.matrix:
            pygame.draw.rect(self.window, pygame.Color('white'), pygame.Rect(coords[0] * self.zoom, coords[1] * self.zoom, self.zoom, self.zoom))

        pygame.display.flip()

        # logic update
        self.structure.update()

        # clock ticking
        self.clock.tick(60)