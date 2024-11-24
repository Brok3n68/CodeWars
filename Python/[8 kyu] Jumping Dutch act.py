# https://www.codewars.com/kata/570bcd9715944a2c8e000009

def sc(n: int) -> str:
    if n <= 1:
        return ""
    
    scream = "Aa~ " * (n - 1)
    impact = "Pa!"
    final_sound = " Aa!" if n <= 6 else ""
    
    return f"{scream}{impact}{final_sound}"