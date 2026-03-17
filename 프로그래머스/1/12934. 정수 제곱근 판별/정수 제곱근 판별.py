import math

def solution(n):
    answer = 0
    
    x = math.isqrt(n)
    
    if x * x == n:
        return (x + 1) ** 2
    
    return -1