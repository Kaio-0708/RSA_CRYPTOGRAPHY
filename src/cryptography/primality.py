# teste probabilístico de primalidade — o Miller–Rabin, no qual se baseia no Teorema de Fermat. Forma do teste: n−1= 2^r⋅d, com d ímpar
import random

# Optei por implementar a Exponenciação Modular Rápida (a^b mod n) em vez de usar pow() da biblioteca.
def mod_exp(a, b, n):
    result = 1
    a = a % n
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        a = (a * a ) % n
        b //= 2
    return result

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

    for i in range(k):
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
