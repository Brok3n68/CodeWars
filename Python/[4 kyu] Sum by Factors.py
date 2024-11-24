# https://www.codewars.com/kata/54d496788776e49e6b00052f

import math
from collections import defaultdict
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_factors(n):
    n = abs(n)
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if is_prime(i):
                factors.add(i)
            n //= i
    if n > 2 and is_prime(n):
        factors.add(n)
    return factors
def sum_for_list(lst):
    if not lst:
        return []
    prime_sum = defaultdict(int)
    for num in lst:
        factors = prime_factors(num)
        for prime in factors:
            prime_sum[prime] += num
    result = sorted([[prime, prime_sum[prime]] for prime in prime_sum])
    
    return result