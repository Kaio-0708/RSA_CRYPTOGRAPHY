#Estrutura baseada no RSA matemático puro, criptografa e decripta uma mensagem numérica m.
from .number_theory import mod_exp, mod_inv, gcd, phi_euller
import random

def escolher_e(phi_euller):
    while True:
        e = random.randint(2, phi_euller - 1)
        if gcd(e, phi_euller) == 1:
            return e

def rsa_math(p, q, m):
    n = p * q
    phi = phi_euller(p, q)
    e = escolher_e(phi)
    d = mod_inv(e, phi)
    criptografar = mod_exp(m, e, n)
    decriptografar = mod_exp(criptografar, d, n)

    if decriptografar != m:
        raise ValueError("Falha na descriptografia")

    return {
    "n": n,
    "phi": phi,
    "e": e,
    "d": d,
    "mensagem": m,
    "criptografar": criptografar,
    "decriptografar": decriptografar
}