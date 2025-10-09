from src.cryptography.rsa_com_texto import rsa_texto

def test_rsa_texto_execucao():
    """Teste simples de execução do RSA com texto"""
    p, q = 61, 53
    mensagem = "A"
    
    resultado = rsa_texto(p, q, mensagem)
    
    assert isinstance(resultado, dict)
    assert resultado["mensagem"] == mensagem
    assert resultado["mensagem_recuperada"] == mensagem

def test_rsa_texto_estrutura():
    """Verifica se retorna todas as chaves esperadas"""
    p, q = 61, 53
    mensagem = "B"
    
    resultado = rsa_texto(p, q, mensagem)
    
    chaves_esperadas = {
        "n", "phi", "e", "d",
        "mensagem", "criptografar",
        "decriptografar", "mensagem_recuperada"
    }
    
    assert set(resultado.keys()) == chaves_esperadas

def test_rsa_texto_valores_matematicos():
    """Verifica valores matemáticos básicos"""
    p, q = 61, 53
    mensagem = "C"
    
    resultado = rsa_texto(p, q, mensagem)
    
    assert resultado["n"] == p * q
    assert resultado["phi"] == (p - 1) * (q - 1)
    assert (resultado["e"] * resultado["d"]) % resultado["phi"] == 1