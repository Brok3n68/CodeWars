# https://www.codewars.com/kata/51c8991dee245d7ddf00000e

def reverse_words(s):
    x = s.split(" ")
    newString = ""
    for i in x[::-1]:
        newString += " " + i 
    newString = newString.strip()
    return newString