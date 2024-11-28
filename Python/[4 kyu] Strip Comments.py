# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def strip_comments(strng, markers):
    lines = strng.split("\n")
    for i in range(len(lines)):
        for marker in markers:
            if marker in lines[i]:
                print(f'lines[i] before: {lines[i]}')
                lines[i] = lines[i].split(marker)[0].rstrip()
                print(f'lines[i] after: {lines[i]}')
    return "\n".join(lines)
