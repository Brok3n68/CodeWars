# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python

def generate_sequences(length, start=1):
    if length == 1:
        for num in range(start, 10):
            yield [num]
    else:
        for num in range(start, 10):
            for seq in generate_sequences(length - 1, num):
                yield [num] + seq

def find_matching_numbers(target_sum, digits):
    valid_numbers = [seq for seq in generate_sequences(digits) if sum(seq) == target_sum]
    if not valid_numbers:
        return []
    return [len(valid_numbers), int("".join(map(str, valid_numbers[0]))), int("".join(map(str, valid_numbers[-1])))]
