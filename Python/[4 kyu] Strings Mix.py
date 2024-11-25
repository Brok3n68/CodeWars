# https://www.codewars.com/kata/5629db57620258aa9d000014

def mix(s1, s2):
    s1 = [char for char in s1 if char.islower()]
    s2 = [char for char in s2 if char.islower()]
    s1_dict = {char: s1.count(char) for char in set(s1) if s1.count(char) > 1}
    s2_dict = {char: s2.count(char) for char in set(s2) if s2.count(char) > 1}
    result = []
    for char in set(s1 + s2):
        if char in s1_dict and char in s2_dict:
            if s1_dict[char] > s2_dict[char]:
                result.append(f"1:{char * s1_dict[char]}")
            elif s1_dict[char] < s2_dict[char]:
                result.append(f"2:{char * s2_dict[char]}")
            else:
                result.append(f"=:{char * s1_dict[char]}")
        elif char in s1_dict:
            result.append(f"1:{char * s1_dict[char]}")
        elif char in s2_dict:
            result.append(f"2:{char * s2_dict[char]}")
    return "/".join(sorted(result, key=lambda x: (-len(x), x)))
