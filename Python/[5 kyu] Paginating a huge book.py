# https://www.codewars.com/kata/55905b7597175ffc1a00005a

def page_digits(pages):
    total, start, tens = 0, 0, 10
    while pages > start:
        total += pages - start
        start = tens - 1
        tens *= 10
    return total    