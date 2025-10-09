# Estrutura meramente para aprendizado, no qual o "m" é uma mensagem de texto, sem padding. 
from cryptography.number_theory import mod_exp, mod_inv, phi_euller
from Utils.text_encoding import texto_para_numero, numero_para_texto
from cryptography.rsa_math import escolher_e

def rsa_texto(p, q, mensagem):
    n = p * q
    phi = phi_euller(p, q)
    e = escolher_e(phi)
    d = mod_inv(e, phi)
   
    m = texto_para_numero(mensagem)
    
    c = mod_exp(m, e, n)
    decrip = mod_exp(c, d, n)
    texto_d = numero_para_texto(decrip)

    if texto_d != mensagem:
        raise ValueError("Falha na descriptografia")
    
    return {
    "n": n,
    "phi": phi,
    "e": e,
    "d": d,
    "mensagem": mensagem,
    "criptografar": c,
    "decriptografar": decrip,
    "texto_d": texto_d 
}