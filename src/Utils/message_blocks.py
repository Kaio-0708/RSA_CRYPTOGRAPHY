#Implementação da divisão de mensagens em blocos com padding PKCS#1 v1.5 para RSA. O padding PKCS#1 v1.5 segue o formato:  0x00 || 0x02 || bytes_aleatorios (≠ 0x00) || 0x00 || dados
import os

def adicionar_padding(bloco, tamanho_bloco_max):
    if tamanho_bloco_max < 11:
        if len(bloco) > tamanho_bloco_max - 3: 
            raise ValueError(f"Bloco muito grande para padding. Dados: {len(bloco)}, Máximo: {tamanho_bloco_max - 3}")
        
        padding_length = tamanho_bloco_max - len(bloco) - 3
        
        if padding_length < 1:  
            padding_length = 1
            
        padding = b''
        while len(padding) < padding_length:
            byte = os.urandom(1)
            if byte != b'\x00':
                padding += byte
        
        bloco_com_padding = b'\x00\x02' + padding + b'\x00' + bloco
        
        if len(bloco_com_padding) < tamanho_bloco_max:
            bloco_com_padding += os.urandom(tamanho_bloco_max - len(bloco_com_padding))
        elif len(bloco_com_padding) > tamanho_bloco_max:
            bloco_com_padding = bloco_com_padding[:tamanho_bloco_max]
            
        return bloco_com_padding
    else:
        tamanho_dados = len(bloco)
        padding_length = tamanho_bloco_max - tamanho_dados - 3
        
        if padding_length < 8:
            raise ValueError(f"Bloco muito grande para padding. Dados: {tamanho_dados}, Máximo: {tamanho_bloco_max - 11}")
        
        padding = b''
        while len(padding) < padding_length:
            byte = os.urandom(1)
            if byte != b'\x00':
                padding += byte
        
        bloco_com_padding = b'\x00\x02' + padding + b'\x00' + bloco
        
        if len(bloco_com_padding) != tamanho_bloco_max:
            raise ValueError(f"Tamanho do bloco incorreto. Esperado: {tamanho_bloco_max}, Obtido: {len(bloco_com_padding)}")
        
        return bloco_com_padding

def remover_padding(bloco_padded):
    if len(bloco_padded) < 4:  
        raise ValueError("Bloco muito curto para conter padding válido")
    
    if bloco_padded[0] != 0x00 or bloco_padded[1] != 0x02:
        raise ValueError("Padding inválido - deve começar com 0x00 0x02")
    
    separador = bloco_padded.find(b'\x00', 2)
    
    if separador == -1:
        raise ValueError("Separador 0x00 não encontrado")
    
    if separador < 3: 
        raise ValueError("Padding muito curto")
    
    if len(bloco_padded) >= 11:
        for i in range(2, separador):
            if bloco_padded[i] == 0x00:
                raise ValueError("Bytes de padding não podem ser 0x00")
    
    return bloco_padded[separador + 1:]

def dividir_blocos(mensagem_bytes, n):
    tamanho_bloco_max = (n.bit_length() + 7) // 8
    
    if tamanho_bloco_max == 4: 
        raise ValueError(f"Chave muito pequena - tamanho máximo do bloco: {tamanho_bloco_max}")
    
    if tamanho_bloco_max < 8:  
        raise ValueError(f"Chave muito pequena - tamanho máximo do bloco: {tamanho_bloco_max}")

    if tamanho_bloco_max < 11:
        tamanho_dados = tamanho_bloco_max - 3
        if tamanho_dados <= 0:
            raise ValueError("Chave muito pequena para conter dados")
    else:
        tamanho_dados = tamanho_bloco_max - 11
    
    blocos = []
    
    for i in range(0, len(mensagem_bytes), tamanho_dados):
        bloco = mensagem_bytes[i:i + tamanho_dados]
        bloco_com_padding = adicionar_padding(bloco, tamanho_bloco_max)
        blocos.append(bloco_com_padding)
    
    return blocos