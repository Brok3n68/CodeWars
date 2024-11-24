# https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic(number):
    sum = 0
    for i in str(number):
        sum += int(i)**(len(str(number)))
    if sum == number:
        return True
    else:
        return False