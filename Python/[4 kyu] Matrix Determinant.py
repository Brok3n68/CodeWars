# https://www.codewars.com/kata/52a382ee44408cea2500074c

# Laplace Expansion for the Determinant of an NxN Matrix:
#
# det(A) = Σ (-1)^i * a_0i * det(M_0i)
#
# Where:
# - det(A) is the determinant of the matrix A.
# - a_0i is the element in the first row and i-th column of the matrix A.
# - M_0i is the minor matrix formed by removing the first row and the i-th column of A.
# - The summation (Σ) is over all columns (i = 0 to n-1) of the first row.
#
# Example:
# For a 3x3 matrix:
#
# A = | a11  a12  a13 |
#     | a21  a22  a23 |
#     | a31  a32  a33 |
#
# det(A) = a11 * det(| a22  a23 |
#                    | a32  a33 |)
#         - a12 * det(| a21  a23 |
#                    | a31  a33 |)
#         + a13 * det(| a21  a22 |
#                    | a31  a32 |)


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += (-1) ** i * matrix[0][i] * determinant([row[:i] + row[i + 1:] for row in matrix[1:]])
        return det