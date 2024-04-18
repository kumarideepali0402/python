Gauss elimination and jordan
def transpose(matrix):
     for j in range(len(matrix))] :
       for i in range(len(matrix[0]))]:
         return [[matrix[j][i]
def matrix_minor(matrix, i, j):
    for row in (matrix[:i]+matrix[i+1:])]
         return [row[:j] + row[j+1:];

def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        det += ((-1)**c)*matrix[0][c]*determinant(matrix_minor(matrix,0,c))
    return det

def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("The matrix is singular, it does not have an inverse.")
    if len(matrix) == 2:
        return [[matrix[1][1]/det, -1*matrix[0][1]/det],
                [-1*matrix[1][0]/det, matrix[0][0]/det]]
    
    cofactors = []
    for r in range(len(matrix)):
        cofactor_row = []
        for c in range(len(matrix)):
            minor = matrix_minor(matrix,r,c)
            cofactor_row.append(((-1)**(r+c)) * determinant(minor))
        cofactors.append(cofactor_row)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/det
    return cofactors

# Example usage:
matrix = [[4, 7, 3],
          [2, 5, 8],
          [1, 0, 6]]

inverse_matrix = inverse(matrix)
for row in inverse_matrix:
    print(row)
