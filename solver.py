class Solver():
    def __init__(self):
        pass

    def find_first_nonzero_row(self, matrix, row, column):
        for row in range(row, matrix.n_rows+1):
            element = matrix.get_element(row, column)
            if element != 0:
                return row, element
        return None, None

    def make_upper_triangular(self, matrix):
        for column in range(1, matrix.n_cols+1):
            nonzero_ind, nonzero_el = self.find_first_nonzero_row(matrix, column, column)
            if nonzero_ind is None:
                continue
            if nonzero_ind != column:
                matrix.switch_rows(column, nonzero_ind)
            for row in range(column, matrix.n_rows+1):
                element = matrix.get_element(row, column)
                if element == 0:
                    continue
                matrix.add_multiply_row(row, column, -element/nonzero_el)
        return matrix

    def solve_system(self, matrix, y):
        if matrix.determinant() == 0:
            raise ValueError("Matrix can't have determinant = 0!")
        m_y = self.build_augmented_matrix(matrix, y)