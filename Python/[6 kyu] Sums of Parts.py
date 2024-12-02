# https://www.codewars.com/kata/5ce399e0047a45001c853c2b

def parts_sums(ls):
    result = [0]
    for x in reversed(ls):
        print(x)
        result.append(result[-1] + x)
        print(result)
    return result[::-1]