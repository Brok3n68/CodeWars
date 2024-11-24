# https://www.codewars.com/kata/5656b6906de340bd1b0000ac

def longest(a1, a2):
    newString = ""
    addedLongest = "".join(a1)
    addedLongest = addedLongest.join(a2)
    addedLongest = sorted(addedLongest)

    for i in addedLongest:
        if i not in newString:
            newString += i

    return newString