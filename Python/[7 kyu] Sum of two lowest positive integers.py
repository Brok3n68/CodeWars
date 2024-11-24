# https://www.codewars.com/kata/558fc85d8fd1938afb000014

def sum_two_smallest_numbers(numbers):
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")
    
    smallest = min(numbers)
    second_smallest = min(num for num in numbers if num != smallest)
    
    return smallest + second_smallest