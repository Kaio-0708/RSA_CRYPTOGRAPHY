
from src.cryptography.rsa_padding import rsa_padding

def test_rsa_padding_execucao():
    """Teste simples de execução do RSA com padding"""
    p, q = 1000000007, 1000000009  
    mensagem = "OLA"
    
    resultado = rsa_padding(p, q, mensagem)
    
    assert isinstance(resultado, dict)
    assert resultado["mensagem_original"] == mensagem
    assert resultado["mensagem_decifrada"] == mensagem

def test_rsa_padding_estrutura():
    """Verifica se retorna todas as chaves esperadas"""
    p, q = 1000000007, 1000000009
    mensagem = "TEST"
    
    resultado = rsa_padding(p, q, mensagem)
    
    chaves_esperadas = {
        "n", "phi", "e", "d",
        "mensagem_original", "blocos_criptografados",
        "blocos_decriptografados", "mensagem_decifrada"
    }
    
    assert set(resultado.keys()) == chaves_esperadas

def test_rsa_padding_valores_matematicos():
    """Verifica valores matemáticos básicos"""
    p, q = 1000000007, 1000000009
    mensagem = "A"
    
    resultado = rsa_padding(p, q, mensagem)
    
    assert resultado["n"] == p * q
    assert resultado["phi"] == (p - 1) * (q - 1)
    assert (resultado["e"] * resultado["d"]) % resultado["phi"] == 1