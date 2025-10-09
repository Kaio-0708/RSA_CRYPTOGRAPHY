from src.Utils.text_encoding import texto_para_numero, numero_para_texto, bytes_para_int, int_para_bytes, converter_str_bytes

def test_converter_str_bytes():
    texto = "RSA"
    b = converter_str_bytes(texto)
    assert isinstance(b, bytes)
    assert b == b"RSA"

def test_bytes_para_int_e_int_para_bytes():
    original_bytes = b"TEST"
    n = bytes_para_int(original_bytes)
    reconstruido_bytes = int_para_bytes(n, len(original_bytes))
    assert reconstruido_bytes == original_bytes

def test_int_para_bytes_erro():
    n = 65536  
    try:
        int_para_bytes(n, 2)
        assert False, "Deveria ter lançado ValueError"
    except ValueError:
        pass  

def test_texto_para_numero_e_numero_para_texto():
    texto = "Hello"
    numero = texto_para_numero(texto)
    texto_recuperado = numero_para_texto(numero)
    assert texto_recuperado == texto

def test_numero_para_texto_0():
    assert numero_para_texto(0) == ""