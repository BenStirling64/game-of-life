import random
import pygame


class Board:
    def __init__(self, width, height):
        pygame.init()

        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.matrix = [[random.randint(0, 1) for j in range(self.width)] for i in range(self.height)]
        self.display = pygame.display
        self.window = self.display.set_mode((width, height))


    def tick(self):
        # inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        # drawing
        self.window.fill('black')

        for row in range(self.height):
            for column in range(self.width):
                if self.matrix[row][column] == 1:
                    pygame.draw.rect(self.window, pygame.Color('white'), pygame.Rect(column, row, 1, 1))

        pygame.display.flip()

        # logic update
        new_matrix = [[self.update_cell(i, j) for j in range(self.width)] for i in range(self.height)]
        self.matrix = new_matrix

        # clock ticking
        self.clock.tick(60)


    def update_cell(self, i, j):
        surrounding_rows = [i - 1, i, i + 1]
        surrounding_columns = [j - 1, j, j + 1]
        surrounding_cells = []
        surrounding_cell_values = []

        if -1 in surrounding_rows:
            surrounding_rows.remove(-1)
        if self.height in surrounding_rows:
            surrounding_rows.remove(self.height)
        if -1 in surrounding_columns:
            surrounding_columns.remove(-1)
        if self.width in surrounding_columns:
            surrounding_columns.remove(self.width)

        for row in surrounding_rows:
            for column in surrounding_columns:
                surrounding_cells.append((row, column))

        surrounding_cells.remove((i, j))

        for cell in surrounding_cells:
            surrounding_cell_values.append(self.matrix[cell[0]][cell[1]])

        if surrounding_cell_values.count(1) == 3:
            return 1
        elif self.matrix[i][j] == 1 and surrounding_cell_values.count(1) == 2:
            return 1
        else:
            return 0