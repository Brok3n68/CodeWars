# https://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True and not None:
            count += 1
    return count