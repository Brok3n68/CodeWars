# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            lst.remove(lst[i])
            lst.append(0)
    return lst