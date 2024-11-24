# https://www.codewars.com/kata/5817030088ca96c0b7000083

def find_characters(matrix):
    lines = matrix.split('\n')
    char_count = {}
    
    for line in lines:
        for char in line:
            if char == '\n':
                continue
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    min_freq = min(char_count.values())

    least_freq_chars = []
    for char, count in char_count.items():
        if count == min_freq:
            least_freq_chars.append(char)

    least_freq_chars.sort(key=lambda x: (x.isdigit(), x.islower(), x))

    return ''.join(least_freq_chars)