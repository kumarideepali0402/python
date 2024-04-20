class Matrix:
    def __init__(self,matrix):
        self.matrix=matrix
    def transpose(self):
        return [[i[j] for j in self.matrix] for i in range(len(self.matrix[0]))]