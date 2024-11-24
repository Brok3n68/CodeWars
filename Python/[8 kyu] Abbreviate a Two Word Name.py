# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3

def abbrev_name(name):
    name = name.upper()
    return f'{name.split(" ")[0][0:1]}.{name.split(" ")[1][0:1]}'