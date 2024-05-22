import random


class BaseMatrix(list):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def get_top_left(self, x, y):
        if x - 1 < 0 or y - 1 < 0:
            raise IndexError

        return (x - 1, y - 1)


    def get_top(self, x, y):
        if y - 1 < 0:
            raise IndexError

        return (x, y - 1)


    def get_top_right(self, x, y):
        if x + 1 >= self.width or y - 1 < 0:
            raise IndexError

        return (x + 1, y - 1)


    def get_left(self, x, y):
        if x - 1 < 0:
            raise IndexError

        return (x - 1, y)


    def get_right(self, x, y):
        if x + 1 >= self.width:
            raise IndexError

        return (x + 1, y)


    def get_bottom_left(self, x, y):
        if x - 1 < 0 or y + 1 >= self.height:
            raise IndexError

        return (x - 1, y + 1)


    def get_bottom(self, x, y):
        if y + 1 >= self.height:
            raise IndexError

        return (x, y + 1)


    def get_bottom_right(self, x, y):
        if x + 1 >= self.width or y + 1 >= self.height:
            raise IndexError

        return (x + 1, y + 1)


    def get_value(self, x, y):
        return self[y][x]


class FTMatrix(BaseMatrix):
    @classmethod
    def blank_verification(cls, width, height):
        matrix = cls(width, height)

        for row in range(height):
            matrix.append([])

            for column in range(width):
                matrix[row].append(False)

        return matrix

    def negate_cell(self, x, y):
        self[y][x] = False


    def activate_cell(self, x, y):
        self[y][x] = True


class NFTMatrix(FTMatrix):
    @classmethod
    def random(cls, width, height):
        matrix = cls(width, height)

        for row in range(height):
            matrix.append([])

            for column in range(width):
                if random.choice([False, True]):
                    matrix[row].append(True)
                else:
                    matrix[row].append(None)

        for row in range(height):
            for column in range(width):
                if matrix[row][column]:
                    matrix.negate_null_neighbours((column, row))

        return matrix


    def deepcopy(self):
        matrix = self.__class__(self.width, self.height)

        for row in range(self.height):
            matrix.append([])

            for column in range(self.width):
                matrix[row].append(self.get_value(column, row))

        return matrix


    def negate_null_neighbours(self, coords):
        try:
            top_left = self.get_top_left(*coords)
            top_left_value = self.get_value(*top_left)
        except IndexError:
            pass
        else:
            if top_left_value is None:
                self.negate_cell(*top_left)

        try:
            top = self.get_top(*coords)
            top_value = self.get_value(*top)
        except IndexError:
            pass
        else:
            if top_value is None:
                self.negate_cell(*top)

        try:
            top_right = self.get_top_right(*coords)
            top_right_value = self.get_value(*top_right)
        except IndexError:
            pass
        else:
            if top_right_value is None:
                self.negate_cell(*top_right)

        try:
            left = self.get_left(*coords)
            left_value = self.get_value(*left)
        except IndexError:
            pass
        else:
            if left_value is None:
                self.negate_cell(*left)

        try:
            right = self.get_right(*coords)
            right_value = self.get_value(*right)
        except IndexError:
            pass
        else:
            if right_value is None:
                self.negate_cell(*right)

        try:
            bottom_left = self.get_bottom_left(*coords)
            bottom_left_value = self.get_value(*bottom_left)
        except IndexError:
            pass
        else:
            if bottom_left_value is None:
                self.negate_cell(*bottom_left)

        try:
            bottom = self.get_bottom(*coords)
            bottom_value = self.get_value(*bottom)
        except IndexError:
            pass
        else:
            if bottom_value is None:
                self.negate_cell(*bottom)

        try:
            bottom_right = self.get_bottom_right(*coords)
            bottom_right_value = self.get_value(*bottom_right)
        except IndexError:
            pass
        else:
            if bottom_right_value is None:
                self.negate_cell(*bottom_right)


    def recursively_tick(self, coords, auxiliary_matrix, verification_matrix):
        self.tick_cell(coords, auxiliary_matrix, verification_matrix)

        try:
            top_left = self.get_top_left(*coords)
            top_left_value = verification_matrix.get_value(*top_left)
        except IndexError:
            pass
        else:
            if not top_left_value:
                self.recursively_tick(top_left, auxiliary_matrix, verification_matrix)

        try:
            top = self.get_top(*coords)
            top_value = verification_matrix.get_value(*top)
        except IndexError:
            pass
        else:
            if not top_value:
                self.recursively_tick(top, auxiliary_matrix, verification_matrix)

        try:
            top_right = self.get_top_right(*coords)
            top_right_value = verification_matrix.get_value(*top_right)
        except IndexError:
            pass
        else:
            if not top_right_value:
                self.recursively_tick(top_right, auxiliary_matrix, verification_matrix)

        try:
            left = self.get_left(*coords)
            left_value = verification_matrix.get_value(*left)
        except IndexError:
            pass
        else:
            if not left_value:
                self.recursively_tick(left, auxiliary_matrix, verification_matrix)

        try:
            right = self.get_right(*coords)
            right_value = verification_matrix.get_value(*right)
        except IndexError:
            pass
        else:
            if not right_value:
                self.recursively_tick(right, auxiliary_matrix, verification_matrix)

        try:
            bottom_left = self.get_bottom_left(*coords)
            bottom_left_value = verification_matrix.get_value(*bottom_left)
        except IndexError:
            pass
        else:
            if not bottom_left_value:
                self.recursively_tick(bottom_left, auxiliary_matrix, verification_matrix)

        try:
            bottom = self.get_bottom(*coords)
            bottom_value = verification_matrix.get_value(*bottom)
        except IndexError:
            pass
        else:
            if not bottom_value:
                self.recursively_tick(bottom, auxiliary_matrix, verification_matrix)

        try:
            bottom_right = self.get_bottom_right(*coords)
            bottom_right_value = verification_matrix.get_value(*bottom_right)
        except IndexError:
            pass
        else:
            if not bottom_right_value:
                self.recursively_tick(bottom_right, auxiliary_matrix, verification_matrix)


    def tick_cell(self, coords, auxiliary_matrix, verification_matrix):
        counter = 0

        try:
            top_left = auxiliary_matrix.get_value(*self.get_top_left(*coords))
        except IndexError:
            pass
        else:
            if top_left is True:
                counter += 1

        try:
            top = auxiliary_matrix.get_value(*self.get_top(*coords))
        except IndexError:
            pass
        else:
            if top is True:
                counter += 1

        try:
            top_right = auxiliary_matrix.get_value(*self.get_top_right(*coords))
        except IndexError:
            pass
        else:
            if top_right is True:
                counter += 1

        try:
            left = auxiliary_matrix.get_value(*self.get_left(*coords))
        except IndexError:
            pass
        else:
            if left is True:
                counter += 1

        try:
            right = auxiliary_matrix.get_value(*self.get_right(*coords))
        except IndexError:
            pass
        else:
            if right is True:
                counter += 1

        try:
            bottom_left = auxiliary_matrix.get_value(*self.get_bottom_left(*coords))
        except IndexError:
            pass
        else:
            if bottom_left is True:
                counter += 1

        try:
            bottom = auxiliary_matrix.get_value(*self.get_bottom(*coords))
        except IndexError:
            pass
        else:
            if bottom is True:
                counter += 1

        try:
            bottom_right = auxiliary_matrix.get_value(*self.get_bottom_right(*coords))
        except IndexError:
            pass
        else:
            if bottom_right is True:
                counter += 1

        if counter == 3 or (counter == 2 and self.get_value(*coords) is True):
            self.activate_cell(*coords)
        else:
            self.negate_cell(*coords)

        verification_matrix.activate_cell(*coords)


    def get_root(self):
        for row in range(self.height):
            for column in range(self.width):
                if self[row][column]:
                    return (column, row)


    def nullify_cell(self, x, y):
        self[y][x] = None

    
    def __str__(self):
        string = ""

        for row in range(self.height):
            string += "|"

            for column in range(self.width):
                if self[row][column] is None or self[row][column] is True:
                    string += str(self[row][column]) + "  "
                else:
                    string += str(self[row][column]) + " "

            string = string[:-1]
            string += "|\n"

        return string.strip()