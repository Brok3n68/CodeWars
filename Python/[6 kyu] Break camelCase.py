# https://www.codewars.com/kata/5208f99aee097e6552000148

def solution(s):
    new_string = ""
    for char in s:
        if char.isupper():
            new_string += " " + char
        else:
            new_string += char
    return new_string.strip()