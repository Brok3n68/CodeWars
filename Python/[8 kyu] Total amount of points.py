# https://www.codewars.com/kata/5bb904724c47249b10000131

def points(games):
    squadPoints = 0
    for i in games:
        x, y = map(int, i.split(':'))
        if x > y:
            squadPoints += 3
        elif x == y:
            squadPoints += 1
    return squadPoints