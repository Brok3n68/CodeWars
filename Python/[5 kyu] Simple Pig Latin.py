# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    splittedText = text.split()
    newText = ""
    for i in splittedText:
        if i.isalpha():
            newText += i[1:] + i[0] + "ay "
        else:
            if i[:-1].isalpha() and i[-1] in "!.?;":
                newText += i[1:-1] + i[0] + "ay" + i[-1] + " "
            else:
                newText += i + " "
    return newText.strip()