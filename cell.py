class Cell:
    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.counter = 0
        self.connections = {(column - 1, row - 1): None, (column, row - 1): None, (column + 1, row - 1): None, (column - 1, row): None, (column + 1, row): None, (column - 1, row + 1): None, (column, row + 1): None, (column + 1, row + 1): None}