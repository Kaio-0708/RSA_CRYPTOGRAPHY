#Implementação da divisão de mensagens em blocos com padding PKCS#1 v1.5 para RSA. O padding PKCS#1 v1.5 segue o formato:  0x00 || 0x02 || bytes_aleatorios (≠ 0x00) || 0x00 || dados
import os

def adicionar_padding(bloco, tamanho_bloco_max):
    padding_length =  tamanho_bloco_max - len(bloco) - 3
    if padding_length < 8:
        raise ValueError(f"Bloco muito grande. Tamanho máximo permitido: {tamanho_bloco_max - 11} bytes")
    
    padding = b''
    
    while len(padding) < padding_length:
        byte = os.urandom(1)
        if byte != b'\x00':
            padding += byte
    
    return b'\x00\x02' + padding + b'\x00' + bloco

def remover_padding(bloco_padded):
    if len(bloco_padded) < 11:
        raise ValueError("Erro: bloco muito curto para conter padding PKCS#1 v1.5")
    
    if bloco_padded[0] != 0x00 or bloco_padded[1] != 0x02:
        raise ValueError("Erro: padding inválido — deve começar com 0x00 0x02")

    separador = bloco_padded.find(b'\x00', 2)

    if separador == -1:
        raise ValueError("Erro: separador 0x00 não encontrado no bloco")

    if separador < 10:
        raise ValueError("Erro: padding muito curto — deve ter pelo menos 8 bytes")
    
    for i in range(2, separador):
        if bloco_padded[i] == 0x00:
            raise ValueError("Bytes de padding não podem ser 0x00")

    mensagem = bloco_padded[separador + 1:]
    return mensagem

def dividir_blocos(mensagem_bytes, n):
    tamanho_bloco_max = (n.bit_length() + 7) // 8
    tamanho_padding = 11
    tamanho_bloco = tamanho_bloco_max - tamanho_padding

    if tamanho_bloco <= 0:
        raise ValueError(f"Chave RSA muito pequena ({n.bit_length()} bits). Mínimo recomendado: 512 bits")

    blocos = []
    
    for i in range(0, len(mensagem_bytes), tamanho_bloco):
        bloco = mensagem_bytes[i:i+tamanho_bloco]
        blocos_padded = adicionar_padding(bloco, tamanho_bloco_max)
        blocos.append(blocos_padded)
    
    return blocos