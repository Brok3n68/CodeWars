# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b

# The Binomial Theorem for (a + b)^n:
# (a + b)^n = Σ [ C(n, k) * a^(n-k) * b^k * x^(n-k) ] for k = 0 to n
# where:
# - Σ denotes the summation (sum over all k from 0 to n)
# - C(n, k) is the binomial coefficient, calculated as:
#   C(n, k) = n! / (k! * (n - k)!)  (also known as "n choose k")
# - a^(n-k) is the term a raised to the power (n-k)
# - b^k is the term b raised to the power k
# - x^(n-k) is the term x raised to the power (n-k), representing the variable part

def expand(expr):
    import re

    match = re.match(r'\(([+-]?\d*)?([a-z])([+-]\d+)\)\^(\d+)', expr)
    if not match:
        return "1"
    
    a_str, x, b_str, n_str = match.groups()
    n = int(n_str)

    if a_str in ("", "+", None):
        a = 1
    elif a_str == "-":
        a = -1
    else:
        a = int(a_str)
    
    b = int(b_str)

    if n == 0:
        return "1"
    if n == 1:
        first_term = f"{a if a != 1 and a != -1 else ('-' if a == -1 else '')}{x}" if a != 0 else ''
        second_term = f"{b}" if b != 0 else ''
        operator = '+' if b > 0 else ''
        return f"{first_term}{operator}{second_term}"
    
    terms = []
    for k in range(n + 1):
        coeff = comb(n, k) * (a ** (n - k)) * (b ** k)
        if coeff == 0:
            continue
        power = n - k
        coeff_abs = abs(coeff)
        
        if coeff_abs != 1 or power == 0:
            coeff_str = f"{coeff_abs}"
        else:
            coeff_str = '' 

        if power == 0:
            term = f"{coeff_str}"
        elif power == 1:
            term = f"{coeff_str}{x}"
        else:
            term = f"{coeff_str}{x}^{power}"
        
        if coeff > 0 and k != 0:
            term = '+' + term
        elif coeff < 0:
            term = '-' + term
        
        terms.append(term)
    
    result = ''.join(terms)
    return result if result[0] != '+' else result[1:]

def comb(n, k):
    from math import comb
    return comb(n, k)
