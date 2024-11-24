# https://www.codewars.com/kata/559a28007caad2ac4e000083

def perimeter(n):
    a, b = 1, 1
    total = a + b
    for _ in range(n - 1):
        a, b = b, a + b
        total += b
    return 4 * total
