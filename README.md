#  RSA Cryptography for Learning

Uma implementação educacional completa do algoritmo RSA em Python, incluindo versão matemática, com texto sem padding e com padding, testes unitários abrangentes e interface de linha de comando.

## Índice

- Visão Geral
- Funcionalidades
- Estrutura do Projeto
- Instalação e Uso
- Testes
- Exemplos de Uso
- Contribuição

## Visão Geral

Este projeto implementa o algoritmo RSA de criptografia de chave pública, demonstrando tanto a teoria matemática quanto aplicações práticas com diferentes esquemas de padding. Desenvolvido para fins educacionais, o sistema inclui implementações completas desde operações matemáticas básicas até criptografia de texto com padding profissional.

## Funcionalidades

### Implementações RSA
- **RSA Matemático**: Operações núcleo do algoritmo
- **RSA com Texto**: Criptografia direta de texto
- **RSA com Padding**: Implementação com PKCS#1 v1.5

### Teoria dos Números
- Exponenciação modular eficiente
- Algoritmo de Euclides estendido
- Cálculo da função φ de Euler
- Geração de números primos (Miller-Rabin)
- Inverso multiplicativo modular

### Utilitários
- Codificação texto/bytes/números
- Divisão de mensagens em blocos
- Sistema de padding PKCS#1 v1.5
- Validação de entrada robusta

### Testes
- 24 testes unitários abrangentes
- Cobertura de casos normais e de erro
- Verificações matemáticas rigorosas

## Estrutura do Projeto

```
├── src/
│ ├── cryptography/
│ │ ├── number_theory.py # Teoria fundamental dos números
│ │ ├── primality.py # Testes de primalidade
│ │ ├── rsa_math.py # Núcleo matemático do RSA
│ │ ├── rsa_texto.py # RSA com texto simples
│ │ └── rsa_padding.py # RSA com padding PKCS#1
│ ├── Utils/
│ │ ├── text_encoding.py # Codificação texto/bytes
│ │ └── message_blocks.py # Divisão e padding de blocos
│ ├── tests/
│ │ ├── test_number_theory.py
│ │ ├── test_primality.py
│ │ ├── test_rsa_math.py
│ │ ├── test_rsa_texto.py
│ │ ├── test_rsa_padding.py
│ │ ├── test_text_encoding.py
│ │ └── test_message_blocks.py
│ ├── cli/
│ │ ├── rsa_math_cli.py
│ │ ├── rsa_texto_cli.py
│ │ └── rsa_padding_cli.py
│ └── main.py # Interface principal
├── requirements.txt
└── README.md
```

## Instalação e Uso

### Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

### Instalação
```
# Clone o repositório
git clone https://github.com/Kaio-0708/RSA_CRYPTOGRAPHY.git
cd RSA_CRYPTOGRAPHY
```
### Execução
```
# Execute o programa principal
python src/main.py
```
### Testes
O projeto inclui uma suite abrangente de testes:
````
# Executar todos os testes
pytest -v
````

## Cobertura de Testes
### 24 testes implementados

### Operações matemáticas (mod_exp, gcd, mod_inv, phi)

### Primalidade (Miller-Rabin)

### Codificação (texto/bytes/números)

### Padding e blocos (PKCS#1 v1.5)

### Cenários de erro e validações

<img width="298" height="157" alt="image" src="https://github.com/user-attachments/assets/d869ec26-be57-4d3c-937d-72345e98b089" />


### Exemplos de Uso
<img width="290" height="157" alt="image" src="https://github.com/user-attachments/assets/39239899-d7dd-40a0-8649-8ad5f023b758" />

## Estrutura de Contribuição

#### Fork do projeto

#### Branch para feature (git checkout -b feature/nova-funcionalidade)

#### Commit das mudanças (git commit -am 'Adiciona nova funcionalidade')

#### Push para o branch (git push origin feature/nova-funcionalidade)

#### Pull Request

## Limitações Conhecidas

#### Performance: Para uso educacional, não otimizado para números extremamente grandes

#### Segurança: Implementação educacional, não para uso em produção

#### Tamanho de Chave: Requer primos suficientemente grandes para padding PKCS#1


## Autor

Kaio Vitor - [GitHub](https://github.com/Kaio-0708)

