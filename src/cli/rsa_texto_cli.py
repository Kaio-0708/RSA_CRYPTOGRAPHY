from ..cryptography.primality import primo_miller_rabin
from ..cryptography.rsa_com_texto import rsa_texto
from ..Utils.text_encoding import texto_para_numero

def executar_rsa_texto():
    while True:
        print("--- RSA com Texto ---")
        
        try:
            p = int(input("Digite o primo p: "))
            if not primo_miller_rabin(p):
                raise ValueError("p não é um número primo.")
            
            q = int(input("Digite o primo q: "))
            if not primo_miller_rabin(q):
                raise ValueError("q não é um número primo.")
            
            if p == q:
                raise ValueError("p e q devem ser primos diferentes.")
            
            mensagem = input("Digite a mensagem: ")
            
            if not mensagem:
                raise ValueError("Mensagem não pode ser vazia")
            
            mensagem_validar = texto_para_numero(mensagem)
            if mensagem_validar >= p * q:
                raise ValueError("Mensagem muito grande para os primos escolhidos.")
            
            resultado = rsa_texto(p, q, mensagem)
            break
        
        except ValueError as falha:
            print("Erro:", falha)
            print("Tente novamente.\n")
    
    print("\n=== Resultado RSA com Texto ===")
    print(f"n = {resultado['n']}")
    print(f"phi = {resultado['phi']}")
    print(f"e (chave pública) = {resultado['e']}")
    print(f"d (chave privada) = {resultado['d']}")
    print(f"Mensagem original: {resultado['mensagem']}")
    print(f"Mensagem criptografada (número): {resultado['criptografar']}")
    print(f"Mensagem decriptografada (número): {resultado['decriptografar']}")
    print(f"Mensagem recuperada: {resultado['texto_d']}")
    print(f"--- Detalhes da Conversão ---")
    print(f"Mensagem → Número: {texto_para_numero(resultado['mensagem'])}")
    print(f"Número → Mensagem: {resultado['texto_d']}")
    
    if resultado["mensagem"] == resultado["texto_d"]:
        print("Verificação:  descriptografia bem-sucedida!")
        
    else:
        print("Verificação: erro na descriptografia!")