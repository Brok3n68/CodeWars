# https://www.codewars.com/kata/56b2abae51646a143400001d

def mystery(n):
    return n ^ (n >> 1)

def mystery_inv(n):
    p = n
    while n:
        n >>= 1
        p ^= n
    return p

def name_of_mystery():
    return "Gray code"
