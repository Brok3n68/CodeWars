# https://www.codewars.com/kata/55f89832ac9a66518f000118/train/python

import re
from collections import defaultdict

def simplify(poly):
    h = defaultdict(int)

    terms = re.findall(r'[+-]?[^+-]+', poly)
    
    for term in terms:
        match = re.match(r'([+-]?\d*)([a-z]+)', term)
        if match:
            k, m = match.groups()
            m = ''.join(sorted(m))
            k = int(k) if k and k not in ['+', '-'] else int(k + '1')
            h[m] += k

    filtered_terms = {m: k for m, k in h.items() if k != 0}
    sorted_terms = sorted(filtered_terms.items(), key=lambda x: (len(x[0]), x[0]))

    result = []
    for i, (m, k) in enumerate(sorted_terms):
        sign = '-' if k < 0 else ('+' if i > 0 else '')
        coefficient = '' if abs(k) == 1 else str(abs(k))
        result.append(f"{sign}{coefficient}{m}")
    
    return ''.join(result)