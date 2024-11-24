# https://www.codewars.com/kata/57cf50a7eca2603de0000090

def move_ten(st):
    newMessage = ""
    for char in st:
        if char.isalpha():
            ascii_val = ord(char.lower())
            new_ascii = ((ascii_val - 97 + 10) % 26) + 97
            newMessage += chr(new_ascii)
        else:
            newMessage += char
    return newMessage