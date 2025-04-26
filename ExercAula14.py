# 1: Verificando se o número é par ou ímpar

# def verificar_par_ou_impar(n):
#     match n % 2:
#         case 0:
#             print(f"{n} é par")
#         case _:
#             print(f"{n} é ímpar")

# # Testando
# verificar_par_ou_impar(4)  # Saída: 4 é par
# verificar_par_ou_impar(7)  # Saída: 7 é ímpar


# 2: Verificando se um número é positivo, negativo ou zero

# def verificar_signo(n):
#     match n:
#         case 0:
#             print("O número é zero")
#         case x if x > 0:
#             print(f"{n} é positivo")
#         case _:
#             print(f"{n} é negativo")

# # Testando
# verificar_signo(10)  # Saída: 10 é positivo
# verificar_signo(-5)  # Saída: -5 é negativo
# verificar_signo(0)   # Saída: O número é zero

# 3: Verificando se uma string é vazia ou não

# def verificar_string(s):
#     match s:
#         case "":
#             print("A string está vazia")
#         case _:
#             print("A string não está vazia")

# # Testando
# verificar_string("")    # Saída: A string está vazia
# verificar_string("Oi")  # Saída: A string não está vazia


# 4: Verificando se um número é maior, menor ou igual a 10

# def verificar_numero_10(n):
#     match n:
#         case x if x > 10:
#             print(f"{n} é maior que 10")
#         case x if x < 10:
#             print(f"{n} é menor que 10")
#         case 10:
#             print("O número é igual a 10")

# # Testando
# verificar_numero_10(15)  # Saída: 15 é maior que 10
# verificar_numero_10(5)   # Saída: 5 é menor que 10
# verificar_numero_10(10)  # Saída: O número é igual a 10


# 5: Classificando uma idade em faixas etárias -  criança, jovem, adulto, idoso

# def classificar_idade(idade):
#     match idade:
#         case x if x <= 12:
#             print("Criança")
#         case x if 13 <= x <= 17:
#             print("Jovem")
#         case x if 18 <= x <= 64:
#             print("Adulto")
#         case x if x >= 65:
#             print("Idoso")

# # Testando
# classificar_idade(10)  # Saída: Criança
# classificar_idade(16)  # Saída: Jovem
# classificar_idade(30)  # Saída: Adulto
# classificar_idade(70)  # Saída: Idoso

# # 1: Verificando se o número é par ou ímpar

# def verificar_par_ou_impar(n):
#     match n % 2:
#         case 0:
#             print(f"{n} é par")
#         case _:
#             print(f"{n} é ímpar")

# # Entrada do usuário
# n = int(input("Digite um número: "))
# verificar_par_ou_impar(n)


# # 2: Verificando se um número é positivo, negativo ou zero
# def verificar_signo(n):
#     match n:
#         case 0:
#             print("O número é zero")
#         case x if x > 0:
#             print(f"{n} é positivo")
#         case _:
#             print(f"{n} é negativo")

# # Entrada do usuário
# n = int(input("Digite um número: "))
# verificar_signo(n)


# # 3: Verificando se uma string é vazia ou não
# def verificar_string(s):
#     match s:
#         case "":
#             print("A string está vazia")
#         case _:
#             print("A string não está vazia")

# # Entrada do usuário
# s = input("Digite uma string: ")
# verificar_string(s)



# # 4: Verificando se um número é maior, menor ou igual a 10
# def verificar_numero_10(n):
#     match n:
#         case x if x > 10:
#             print(f"{n} é maior que 10")
#         case x if x < 10:
#             print(f"{n} é menor que 10")
#         case 10:
#             print("O número é igual a 10")

# # Entrada do usuário
# n = int(input("Digite um número: "))
# verificar_numero_10(n)


def classificar_idade(idade):
    match idade:
        case x if x <= 12:
            print("Criança")
        case x if 13 <= x <= 17:
            print("Jovem")
        case x if 18 <= x <= 64:
            print("Adulto")
        case x if x >= 65:
            print("Idoso")

# Entrada do usuário
idade = int(input("Digite sua idade: "))
classificar_idade(idade)
