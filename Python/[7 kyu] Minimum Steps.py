# https://www.codewars.com/kata/5a91a7c5fd8c061367000002

def minimum_steps(numbers, value):
    numbers.sort()
    count = 0
    sum = 0
    
    for i in numbers:
        sum += i
        if sum >= value:
            return count
        count += 1
        
    return 0