def converter_str_bytes(mensagem):
    return mensagem.encode("utf-8")

def bytes_para_int(bloco_bytes):
    m = 0
    for b in bloco_bytes:
        m = m * 256 + b
    return m

def int_para_bytes(n, tamanho):
    if n >= 256 ** tamanho:
        raise ValueError(f"Tamanho insuficiente para representar o número")
    
    bytes_lista = []
    for _ in range(tamanho):
        bytes_lista.append(n % 256)
        n = n // 256
    
    if n > 0:
        raise ValueError(f"Tamanho insuficiente para representar o número")
    
    bytes_lista.reverse()
    return bytes(bytes_lista)

def texto_para_numero(texto):
    m = 0
    for b in texto.encode("utf-8"):
        m = m * 256 + b
    return m

def numero_para_texto(m):
    if m == 0:
        return ""
    
    bytes_lista = []
    while m > 0:
        bytes_lista.append(m % 256)
        m //= 256
    bytes_lista.reverse()
    return bytes(bytes_lista).decode("utf-8")