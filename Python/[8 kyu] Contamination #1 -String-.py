# https://www.codewars.com/kata/596fba44963025c878000039

def contamination(text, char):
    if not text.strip():
        return ""
    for i in text:
        text = text.replace(i, char)
    return text