# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26

def fib(n):
    if n == 0:
        return 0
        
    def fib_positive(n):
        if n == 0:
            return (0, 1)

        m = n >> 1
        a, b = fib_positive(m)
        c = a * ((b << 1) - a)
        d = a * a + b * b
        
        if n & 1:
            return (d, c + d)
        else:
            return (c, d)
    
    #F(-n) = (-1)^(n+1) * F(|n|) 
    if n < 0:
        return (-1)**(abs(n) + 1) * fib_positive(abs(n))[0]
    else:
        return fib_positive(n)[0]