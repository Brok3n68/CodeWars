# https://www.codewars.com/kata/5426d7a2c2c7784365000783/train/python

def balanced_parens(n):
    ret = []

    def generate(p, o, c):
        if o == n and c == n:
            ret.append(p)
            return
        elif o == n:
            ret.append(p+")"*(n-c))
            return
        
        if o > c:
            generate(p + ")", o, c + 1)
        generate(p + "(", o+1, c)
    
    generate("", 0, 0)
    
    return ret