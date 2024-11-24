# https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    hexValue = ""

    if r < 0:
        r = 0
    elif r > 255:
        r = 255

    if g < 0:
        g = 0
    elif g > 255:
        g = 255

    if b < 0:
        b = 0
    elif b > 255:
        b = 255
    
    r = hex(r).upper()
    g = hex(g).upper()
    b = hex(b).upper()

    r = r.replace("X", "")
    g = g.replace("X", "")
    b = b.replace("X", "")

    if len(r) > 2:
        r = r.replace("0", "", 1)
    
    if len(g) > 2:
        g = g.replace("0", "", 1)

    if len(b) > 2:
        b = b.replace("0", "", 1)

    hexValue = r + g + b

    return hexValue