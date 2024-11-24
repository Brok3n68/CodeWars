# https://www.codewars.com/kata/530e15517bc88ac656000716

def rot13(message):
    newMessage = ""
    for i in message:
        if ord(i) >= 65 and ord(i) <= 90:  # Uppercase letters
            if ord(i) <= 77:  # A-M
                newMessage += chr(ord(i) + 13)
            else:  # N-Z
                newMessage += chr(ord(i) - 13)
        elif ord(i) >= 97 and ord(i) <= 122:  # Lowercase letters
            if ord(i) <= 109:  # a-m
                newMessage += chr(ord(i) + 13)
            else:  # n-z
                newMessage += chr(ord(i) - 13)
        else:  # Non-alphabetic characters
            newMessage += i
    return newMessage