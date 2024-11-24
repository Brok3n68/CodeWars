# https://www.codewars.com/kata/5324945e2ece5e1f32000370

def sum_strings(x, y):
    x = x.lstrip('0')
    y = y.lstrip('0')
    
    if not x: x = '0'
    if not y: y = '0'
    
    if len(y) > len(x):
        x, y = y, x
    
    x = x[::-1]
    y = y[::-1]
    
    carry = 0
    result = []
    
    for i in range(len(x)):
        digit_x = int(x[i])
        digit_y = int(y[i]) if i < len(y) else 0 
        total = digit_x + digit_y + carry
    
        result.append(str(total % 10))
    
        carry = total // 10
    
    if carry:
        result.append(str(carry))
    
    return ''.join(result[::-1])