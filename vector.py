class Vector:
    def __init__(self, vector):
        self.len = len(vector)
        self.content = vector

    def get_element(self, ind):
        if ind < 1:
            raise IndexError("Index should be larger than 0!")
        if ind > self.len:
            raise IndexError("Index should be smaller than vector length!")
        return self.content[ind-1]

    def sum_vectors(self, b):
        if self.len != b.len:
            raise ValueError("Vectors should have same length!")
        return Vector([self.get_element(i) + b.get_element(i) for i in range(1, self.len+1)])

    def subtract_vectors(self, b):
        if self.len != b.len:
            raise ValueError("Vectors should have same length!")
        return Vector([self.get_element(i) - b.get_element(i) for i in range(1, self.len+1)])

    def multiply_vectors(self, b):
        if self.len != b.len:
            raise ValueError("Vectors should have same length!")

        result = 0
        for i in range(1, self.len+1):
            result += self.get_element(i)*b.get_element(i)

        return result