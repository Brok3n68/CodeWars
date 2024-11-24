# https://www.codewars.com/kata/5518a860a73e708c0a000027

# Formula to find the last digit of a number raised to a power:
# 1. Identify the last digit of the base number (n).
# 2. For last digits in {2, 3, 7, 8, 4, 9}:
#    a. Compute the power mod 4 (exponent % 4).
#    b. If the remainder is 0, treat it as 4 (to account for the cycle length).
#    c. Raise the last digit of the base to the computed remainder.
#    d. Extract the last digit of the result.
# 3. For last digits in {0, 1, 5, 6}:
#    The last digit of the number remains the same regardless of the power.
# Example: To find the last digit of 11797^2014:
# - Last digit of base = 7.
# - Power mod 4 = 2014 % 4 = 2.
# - 7^2 = 49, last digit = 9.

def last_digit(lst):
    if lst == []:
        return 1
    result = 1
    for num in lst[::-1]:
        result = num ** (result if result < 4 else result % 4 + 4)
    return result % 10