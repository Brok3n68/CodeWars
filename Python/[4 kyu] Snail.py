# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    if snail_map == [[]]:
        return []
    result = []
    while len(snail_map) > 0:
        result += snail_map[0]
        snail_map = snail_map[1:]
        snail_map = list(zip(*snail_map))[::-1]
    return result
