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