from src.cryptography.rsa_math import rsa_math

def test_rsa_math_execucao():
    p, q, m = 7, 11, 5
    resultado = rsa_math(p, q, m)
    assert isinstance(resultado, dict)