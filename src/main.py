from .cli.rsa_math_cli import executar_rsa_math

def main ():
    while True:
        print = ("""Escolha uma opção:
    1 - RSA matemático
    2 - RSA com texto
    3 - RSA com padding
    0 - Sair """)
        
        try:
            escolha = int(input("Digite uma escolha: "))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        if escolha == 1:
            executar_rsa_math()
        elif escolha == 2:
            executar_rsa_texto()
        elif escolha == 3:
            executar_rsa_padding()
        elif escolha == 0:
            print("Processo finalizado!")
            break
        else:
            print("Opção inválida, selecione outro número.")