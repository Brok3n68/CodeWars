# https://www.codewars.com/kata/5940ec284aafb87ef3000028

def decode(number):
    parts = str(number).split('98')
    sub = []
    
    for i, part in enumerate(parts):
        if not part:
            continue
        if i % 2 == 0:
            text = ''.join(chr(int(part[j:j+3]) - 100 + ord('a') - 1) for j in range(0, len(part), 3))
            sub.append(text)
        else:
            binary = int(part, 2)
            sub.append(str(binary))
    return ', '.join(sub)