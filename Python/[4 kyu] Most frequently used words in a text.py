# https://www.codewars.com/kata/51e056fe544cf36c410000fb

def top_3_words(text):
    res = {}
    textf = ''.join(char.lower() if char.isalpha() or char == ' ' or char == "'" 
                   else ' ' for char in text).split(' ')
    for char in textf:
        if char.replace("'", '').isalpha():
            if char in res:
                res[char] += 1
            else:
                res[char] = 1
    return [i for i, j in sorted(res.items(), key=lambda res: res[1], reverse=True)][:3]