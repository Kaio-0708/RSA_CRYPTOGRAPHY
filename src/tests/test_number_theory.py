from src.cryptography.number_theory import mod_exp, mod_inv, gcd, phi_euller, bezout

def test_mod_exp():
    assert mod_exp(4, 13, 497) == pow(4, 13, 497)

def test_gcd():
    assert gcd(54, 24) == 6

def test_phi_euller():
    assert phi_euller(7, 11) == 60

def test_bezout():
    a, b = 30, 20
    d, x, y = bezout(a, b)
    assert a * x + b * y == d
    assert d == gcd(a, b)

def test_mod_inv():
    assert mod_inv(3, 11) == 4
    assert mod_inv(10, 17) == 12
    