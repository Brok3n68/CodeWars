# https://www.codewars.com/kata/5a34da5dee1aae516d00004a

def get_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
