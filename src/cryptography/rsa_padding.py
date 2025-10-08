#Estrutura baseada no RSA Padding, pois é mais seguro e próximo do uso real do RSA. Porém, aplicando de forma para aprendizado.
from .number_theory import mod_exp, mod_inv, phi_euller
from .rsa_math import escolher_e
from ..Utils.message_blocks import dividir_blocos, remover_padding
from ..Utils.text_encoding import converter_str_bytes, bytes_para_int, int_para_bytes

def rsa_padding(p, q, mensagem):
    n = p * q
    phi = phi_euller(p, q)
    e = escolher_e(phi)
    d = mod_inv(e, phi)

    mensagem_bytes = converter_str_bytes(mensagem)
    blocos = dividir_blocos(mensagem_bytes, n)

    blocos_criptografados = []
    for bloco in blocos:
        m_int = bytes_para_int(bloco)
        c = mod_exp(m_int, e, n)
        blocos_criptografados.append(c)

    blocos_decriptografados = []
    mensagem_recuperada = b""
    tamanho_bloco_max = (n.bit_length() + 7) // 8

    for c in blocos_criptografados:
        m_dec_int = mod_exp(c, d, n)
        bloco_bytes = int_para_bytes(m_dec_int, tamanho_bloco_max)
        bloco_limpo = remover_padding(bloco_bytes)
        blocos_decriptografados.append(m_dec_int)
        mensagem_recuperada += bloco_limpo
    
    try:
        mensagem_decifrada = mensagem_recuperada.decode("utf-8")
    except UnicodeDecodeError as e:
        raise ValueError(f"Erro ao decodificar mensagem recuperada: {e}")

    if mensagem_decifrada != mensagem:
        raise ValueError("A mensagem recuperada não coincide com a original")

    return {
        "n": n,
        "phi": phi,
        "e": e,
        "d": d,
        "mensagem_original": mensagem,
        "blocos_criptografados": blocos_criptografados,
        "blocos_decriptografados": blocos_decriptografados, 
        "mensagem_decifrada": mensagem_recuperada.decode("utf-8", errors="ignore")
    }