from cryptography.primality import primo_miller_rabin
from cryptography.rsa_padding import rsa_padding

def executar_rsa_padding():
    while True:
        print("--- RSA com Padding (PKCS#1 v1.5) ---")
    
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
        
            if len(mensagem) > 1000:
                raise ValueError("Mensagem muito longa. Máximo: 1000 caracteres.")
        
            resultado = rsa_padding(p, q, mensagem)
            break
        
        except ValueError as falha:
            print("Erro:", falha)
            print("Tente novamente.\n")
        
    print("\n=== Resultado RSA com Padding ===")
    print(f"n = {resultado['n']} ({resultado['n'].bit_length()} bits)")
    print(f"phi = {resultado['phi']}")
    print(f"e (chave pública) = {resultado['e']}")
    print(f"d (chave privada) = {resultado['d']}")
    print(f"Mensagem original: {resultado['mensagem_original']}")
    print(f"Quantidade de blocos: {len(resultado['blocos_criptografados'])}")
    print(f"Blocos criptografados: {resultado['blocos_criptografados']}")
    print(f"Blocos decriptografados: {resultado['blocos_decriptografados']}")
    print(f"Mensagem recuperada: {resultado['mensagem_decifrada']}")
    
    if resultado["mensagem_original"] == resultado["mensagem_decifrada"]:
        print("Verificação: descriptografia bem-sucedida!")
        print()
    
    else:
        print("Verificação: erro na descriptografia!")
        print()