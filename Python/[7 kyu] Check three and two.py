# https://www.codewars.com/kata/5a9e86705ee396d6be000091

def check_three_and_two(array):

    count_a, count_b, count_c = 0, 0, 0

    for char in array:
        if char == "a":
            count_a += 1
        elif char == "b":
            count_b += 1
        else:
            count_c += 1

    counts = [count_a, count_b, count_c]

    return 3 in counts and 2 in counts