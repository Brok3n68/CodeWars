# https://www.codewars.com/kata/5511b2f550906349a70004e1

def last_digit(n1, n2):
    try:
        return pow(n1, n2, 10)
    except:
        return 1
    