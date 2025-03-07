# https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

def solution(roman: str) -> int:
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    roman = list(roman)
    result = 0
    for i in range(len(roman)):
        if i+1 < len(roman) and roman_dict[roman[i]] < roman_dict[roman[i+1]]:
            result -= roman_dict[roman[i]]
        else:
            result += roman_dict[roman[i]]

    return result