# Optei por implementar todas as funções manualmente em vez de importar de biblioteca. 

def mod_exp(a, b, n):
    result = 1
    a = a % n
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        a = (a * a ) % n
        b //= 2
    return result

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def bezout(a, b):
    x0, y0 = 1, 0
    x1, y1 = 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    
    return a, x0, y0

def mod_inv(a, n):
    g, x, y = bezout(a, n)
    if g != 1:
        print(f"Inverso modular não existe para {a} mod {n}")
    return x % n

def phi_euller(p, q):
    return (p-1) * (q -1)
    