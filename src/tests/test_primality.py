from src.cryptography.primality import primo_miller_rabin

def test_primo():
    assert primo_miller_rabin(7) is True
    assert primo_miller_rabin(9) is False
