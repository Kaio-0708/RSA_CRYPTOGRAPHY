import pytest
from src.Utils.message_blocks import adicionar_padding, remover_padding, dividir_blocos

def test_adicionar_e_remover_padding():
    bloco = b"HELLO"
    tamanho_max = 32
    bloco_padded = adicionar_padding(bloco, tamanho_max)

    assert len(bloco_padded) == tamanho_max
    assert bloco_padded.startswith(b'\x00\x02')
    assert bloco_padded.endswith(bloco)

    bloco_limpo = remover_padding(bloco_padded)
    assert bloco_limpo == bloco

def test_remover_padding_erro_tamanho_curto():
    bloco_curto = b"\x00\x02abc"
    with pytest.raises(ValueError):
        remover_padding(bloco_curto)

def test_remover_padding_erro_inicio_invalido():
    bloco_invalido = b"\x01\x02" + b"A"*20
    with pytest.raises(ValueError):
        remover_padding(bloco_invalido)

def test_remover_padding_erro_sem_separador():
    bloco_sem_separador = b'\x00\x02' + b'\xFF'*20
    with pytest.raises(ValueError):
        remover_padding(bloco_sem_separador)

def test_dividir_blocos():
    mensagem = b"HELLO WORLD RSA TESTING"
    n = 2**512 
    blocos = dividir_blocos(mensagem, n)
    
    for bloco in blocos:
        assert isinstance(bloco, bytes)
        assert bloco.startswith(b'\x00\x02')
    
    mensagem_recuperada = b"".join(remover_padding(bloco) for bloco in blocos)
    assert mensagem_recuperada == mensagem

def test_dividir_blocos_chave_pequena():
    mensagem = b"TEST"
    n = 2**32 
    with pytest.raises(ValueError):
        dividir_blocos(mensagem, n)