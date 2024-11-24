# https://www.codewars.com/kata/55908aad6620c066bc00002a

def xo(s):
    s = s.lower()
    if s == "":
        return True
    elif s.find("x") and s.find("o") is True:
        return False
    elif s.count("x") == s.count("o"):
        return True
    else:
        return False