# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

def wave(people):
    mexicanWave = []
    
    for i, char in enumerate(people):
        if char != " ":
            tempPeople = people[:i] + char.upper() + people[i+1:]
            mexicanWave.append(tempPeople)
    
    return mexicanWave
