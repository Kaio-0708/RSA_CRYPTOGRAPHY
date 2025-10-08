def converter_str_bytes(mensagem):
    mensagem_bytes = mensagem.encode("utf-8")
    return mensagem_bytes

def bytes_para_int(bloco_bytes):
    m = 0
    for b in bloco_bytes:
        m = m * 256 + b
    return m

def int_para_bytes(n, tamanho):
    
    bytes_lista = []

    for _ in range(tamanho):
        bytes_lista.append(n % 256)
        n = n // 256
    
    if n > 0:
        raise ValueError(f"O tamanho não é suficiente para representar o número")
    
    bytes_lista.reverse()
    return bytes(bytes_lista)