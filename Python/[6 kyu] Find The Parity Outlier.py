# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    evenCount, oddCount = 0, 0
    for i in integers:
        if i % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    if evenCount > oddCount:
        for i in integers:
            if not i % 2 == 0:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i