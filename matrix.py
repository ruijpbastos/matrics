from vector import Vector

class Matrix(Vector):
    def __init__(self, matrix):
        self.n_rows = len(matrix)

        if isinstance(matrix[0], Vector):
            self.n_cols = matrix[0].len
        elif isinstance(matrix[0], list):
            self.n_cols = len(matrix[0])
        
        self.shape = (self.n_rows, self.n_cols)

        self.content = []
        for i in range(len(matrix)):
            if isinstance(matrix[i], Vector):
                self.content.append(matrix[i])
            elif isinstance(matrix[i], list):
                self.content.append(Vector(matrix[i]))
            else:
                raise ValueError("Rows must be either lists or Vectors!")

    def show(self):
        for vector in self.content:
            vector.show()

    def get_row(self, row_ind):
        if row_ind < 1:
            raise IndexError("Row index should be larger than 0!")
        if row_ind > self.n_rows:
            raise IndexError("Row index should be smaller than number of columns!")
        return self.content[row_ind-1]

    def get_column(self, col_ind):
        if col_ind < 1:
            raise IndexError("Column index should be larger than 0!")
        if col_ind > self.n_cols:
            raise IndexError("Column index should be smaller than number of columns!")
        return Vector([self.get_row(i).get_element(col_ind) for i in range(1, self.n_rows+1)])

    def get_element(self, row_ind, col_ind):
        if row_ind < 1:
            raise IndexError("Row index should be larger than 0!")
        if col_ind < 1:
            raise IndexError("Column index should be larger than 0!")
        if row_ind > self.n_rows:
            raise IndexError("Row index should be smaller than number of rows!")
        if col_ind > self.n_cols:
            raise IndexError("Column index should be smaller than number of columns!")
        return self.get_row(row_ind).get_element(col_ind)

    def sum_matrices(self, b):
        if self.shape != b.shape:
            raise ValueError("Matrices should have same shape!")
        return Matrix([self.get_row(i).sum_vectors(b.get_row(i)) for i in range(1, self.n_rows+1)])

    def subtract_matrices(self, b):
        if self.shape != b.shape:
            raise ValueError("Matrices should have same shape!")
        return Matrix([self.get_row(i).subtract_vectors(b.get_row(i)) for i in range(1, self.n_rows+1)])

    def multiply_matrices(self, b):
        if self.n_cols != b.n_rows:
            raise ValueError("Number of columns of matrix on the left must be equal to the number of rows of matrix on the right!")

        matrix = []
        for i in range(1, self.n_rows+1):
            row = []
            for j in range(1, b.n_cols+1):
                row.append(self.get_row(i).multiply_vectors(b.get_column(j)))
            matrix.append(row)
        return Matrix(matrix)

    def transpose(self):
        return Matrix([self.get_column(i) for i in range(1, self.n_cols+1)])

    def switch_rows(self, i, j):
        self.content[i-1], self.content[j-1] = self.content[j-1], self.content[i-1]

    def multiply_row(self, i, k):
        self.content[i-1] = self.content[i-1].multiply_by_scalar(k)

    def add_row(self, i, j):
        self.content[i-1] = self.content[i-1].sum_vectors(self.content[j-1])

    def add_multiply_row(self, i, j, k):
        temp = self.content[j-1]
        self.multiply_row(j, k)
        self.add_row(i, j)
        self.content[j-1] = temp

    def subtract_row(self, i, j):
        self.add_multiply_row(i, j, -1)

    def switch_columns(self, i, j):
        matrix_t = self.transpose()
        matrix_t.switch_rows(i, j)
        self.content = matrix_t.transpose().content

    def _determinant2by2(self):
        return self.get_element(1, 1)*self.get_element(2, 2) - self.get_element(1, 2)*self.get_element(2, 1)
    
    def remove_row(self, i):
        return Matrix([self.content[j-1] for j in range(1, self.n_rows+1) if j != i])

    def remove_column(self, j):
        matrix = []
        for i in range(1, self.n_rows+1):
            new_row = [self.get_row(i).get_element(k) for k in range(1, self.n_cols+1) if k != j]
            matrix.append(new_row)
        return Matrix(matrix)

    def get_partition(self, i, j):
        return self.remove_row(i).remove_column(j)

    def determinant(self):
        if self.n_rows != self.n_cols:
            raise ValueError("Must be a square matrix!")
        if self.shape == (2, 2):
            return self._determinant2by2()
        determinant = 0
        for i in range(1, self.n_rows+1):
            element = self.get_element(i, 1)
            if element != 0:
                determinant += self.element*(-1)**(i+1)*self.get_partition(i, 1).determinant()
        return determinant
