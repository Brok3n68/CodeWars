# https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python

def dbl_linear(n):
    u = [1]
    i2 = i3 = 0

    for _ in range(n):
        y = 2 * u[i2] + 1
        z = 3 * u[i3] + 1
        next_val = min(y, z)
        u.append(next_val)

        if next_val == y:
            i2 += 1
        if next_val == z:
            i3 += 1

    return u[n]