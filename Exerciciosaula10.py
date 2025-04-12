# Exercício 1 - CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.
''''
def comparar_numeros():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    if num1 % 2 == 0:
        print(f"{num1} é Par")
    else:
        print(f"{num1} é Ímpar")
    
    if num2 % 2 == 0:
        print(f"{num2} é Par")
    else:
        print(f"{num2} é Ímpar")

comparar_numeros()


# Exercício 2 - CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NÚMEROS.

def multiplicar():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))
    resultado = a * b * c
    print("Resultado:", resultado)

multiplicar()


# Exercício 3 - CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

def potencia():
    base = float(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))
    resultado = base ** expoente
    print("Resultado:", resultado)

potencia()


# Exercício 4 - FUNÇÃO PARA MOSTRAR UMA MENSAGEM SE O USUÁRIO TIVER 18 ANOS
def mensagem_personalizada():
    idade = int(input("Digite sua idade: "))
    if idade == 18:
        print("Parabéns! Você tem 18 anos.")
    else:
        print("Você não tem 18 anos.")

mensagem_personalizada()


# Exercício 5 - FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
def calcular_idade():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = 2025
    idade = ano_atual - ano_nascimento
    print("Sua idade é:", idade)

calcular_idade()


# Exercício 6 - FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.
def verificar_copa():
    if 1999 in [1958, 1962, 1970, 1994, 2002]:
        print("O Brasil ganhou a Copa em 1999.")
    else:
        print("O Brasil NÃO ganhou a Copa em 1999.")

verificar_copa()
'''

# Exercício 7 - DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***  

def restaurante():
    print("----- MENU -----")
    print("1 - Salada")
    print("2 - Macarronada")
    print("3 - Sanduíche")
    print("4 - Sorvete")

    opcao = input("Escolha seu prato: ")

    if opcao == '1':
        print("Você escolheu Salada.")
    elif opcao == '2':
        print("Você escolheu Macarronada.")
    elif opcao == '3':
        print("Você escolheu Sanduíche.")
    elif opcao == '4':
        print("Você escolheu Sorvete.")
    else:
        print("Opção inválida.")

restaurante()

