# teste probabilístico de primalidade — o Miller–Rabin, no qual se baseia no Teorema de Fermat. Forma do teste: n−1= 2^r⋅d, com d ímpar
import random
from .number_theory import mod_exp

def primo_miller_rabin(n, k = 10):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //=2

    for _ in range(k):
        a = random.randint(2, n-2)
        x = mod_exp(a, d, n)

        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = mod_exp(x, 2, n)
            if x == n - 1:
                break

        else:
            return False
        
    return True
