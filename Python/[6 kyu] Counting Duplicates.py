# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def duplicate_count(text):
    text = text.lower()
    arr = []
    
    for char in text:
        if (not(char in arr) and text.count(char) > 1):
            arr.append(char)
            
    return len(arr)   