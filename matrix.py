import random
from cell import Cell


class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = {}

        self.randomise()


    def randomise(self):
        for row in range(self.height):
            for column in range(self.width):
                if random.choice([False, True]) and not (column, row) in self.cells:
                    self.cells[(column, row)] = Cell(column, row)

        for coords in self.cells:
            self.add_connections(self.cells[coords])
            

    def add_connections(self, cell):
        for row in range(cell.row - 1, cell.row + 2):
            if row < 0 or row >= self.height:
                    continue

            for column in range(cell.column - 1, cell.column + 2):
                if column < 0 or column >= self.width:
                    continue

                if (column, row) == (cell.column, cell.row):
                    continue
                    
                if (column, row) in self.cells:
                    cell.connections[(column, row)] = self.cells[(column, row)]
                else:
                    cell.connections[(column, row)] = None


    def get_added_cells(self):
        cells_to_be = {}

        for coords in self.cells:
            for connection_coords in self.cells[coords].connections:
                if not connection_coords in self.cells and connection_coords[0] >= 0 and connection_coords[0] < self.width and connection_coords[1] >= 0 and connection_coords[1] < self.height:
                    if not connection_coords in cells_to_be:
                        connection = Cell(*connection_coords)
                        cells_to_be[connection_coords] = connection
                        connection.counter = 1
                    else:
                        cells_to_be[connection_coords].counter += 1

        return cells_to_be


    def get_culled_cells(self):
        cells_to_be = {}

        for coords in self.cells:
            connections = self.cells[coords].connections

            for connection_coords in connections:
                if connection_coords in self.cells:
                    if not connection_coords in cells_to_be:
                        cell = self.cells[connection_coords]

                        cells_to_be[connection_coords] = cell

                        cell.counter += 1
                    else:
                        cells_to_be[connection_coords].counter += 1

        return cells_to_be


    def add_cells(self, cells_to_be):
        for coords in cells_to_be:
            cell = cells_to_be[coords]

            if cell.counter == 3:
                self.cells[coords] = cell
                cell.counter = 0

    
    def cull_cells(self, cells_to_be):
        for coords in cells_to_be:
            cell = cells_to_be[coords]

            if cell.counter >= 2 and cell.counter < 4:
                self.cells[coords] = cell
                cell.counter = 0


    def update(self):
        added_cells = self.get_added_cells()
        culled_cells = self.get_culled_cells()

        self.cells = {}

        self.add_cells(added_cells)
        self.cull_cells(culled_cells)

        for coords in self.cells:
            self.add_connections(self.cells[coords])



