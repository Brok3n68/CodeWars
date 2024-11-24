# https://www.codewars.com/kata/54d512e62a5e54c96200019e

def prime_factors(n):
    factors = {}
    divisor = 2
    
    while divisor * divisor <= n:
        while (n % divisor) == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            n //= divisor
        divisor += 1
    
    if n > 1:
        factors[n] = 1

    result = ''.join(f"({p}" + (f"**{exp}" if exp > 1 else "") + ")" for p, exp in sorted(factors.items()))
    return result