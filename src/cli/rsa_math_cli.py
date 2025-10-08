# Ocorre verificações básicas para o RSA funcionar corretamente. o "m" não pode ser negativo, nem maior que n. Assim como o "p" e "q" não podem ser iguais. 
from ..cryptography.rsa_math import rsa_math
from ..cryptography.primality import primo_miller_rabin

def executar_rsa_math():
    while True:
        print("--- RSA Matemático ---")

        try:
            p = int(input("Digite o primo p: "))
            if not primo_miller_rabin(p):
                raise ValueError("p não é um número primo.")
            
            q = int(input("Digite o primo q: "))
            if not primo_miller_rabin(q):
                raise ValueError("q não é um número primo.")
            
            if p == q:
                raise ValueError("p e q devem ser primos diferentes.")
            
            m = int(input("Digite a mensagem número 'm': "))

            n = p * q
            if m >= n:
                raise ValueError("A mensagem 'm' deve ser menor que 'n'.")
            if m < 0:
                raise ValueError("A mensagem 'm' não pode ser negativa.")
        
            resultado = rsa_math(p, q, m)
            break
        
        except ValueError as falha:
            print("Erro:", falha)
            print("Tente novamente.\n")
    
    print("\n=== Resultado RSA Matemático ===")
    print(f"n = {resultado['n']}")
    print(f"phi = {resultado['phi']}")
    print(f"e (chave pública) = {resultado['e']}")
    print(f"d (chave privada) = {resultado['d']}")
    print(f"Mensagem original: {resultado['mensagem']}")
    print(f"Criptografada: {resultado['criptografar']}")
    print(f"Decriptografada: {resultado['decriptografar']}")
    
    if resultado["mensagem"] == resultado["decriptografar"]:
        print("Verificação:  descriptografia bem-sucedida!")
        
    else:
        print("Verificação: erro na descriptografia!")