# https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    s = ""
    for i in str(num):
        s2 = int(i) ** 2
        s += str(s2)
    return int(s)