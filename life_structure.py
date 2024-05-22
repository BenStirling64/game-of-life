import matrix


class LifeStructure:
    def __init__(self, matrix):
        self.matrix = matrix
        self.root = matrix.get_root()
        self.update = self.unstable_update


    def unstable_update(self):
        auxiliary_matrix = self.matrix.deepcopy()
        verification_matrix = matrix.FTMatrix.blank_verification(self.matrix.width, self.matrix.height)

        self.matrix.recursively_tick(self.root, auxiliary_matrix, verification_matrix)

    def __str__(self):
        return str(self.matrix)