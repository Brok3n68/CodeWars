# https://www.codewars.com/kata/56f6ad906b88de513f000d96

def bonus_time(salary, bonus):
    if bonus == True:
        return "$"+str(salary * 10)
    else:
        return "$"+str(salary)