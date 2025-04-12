# Exercício 1: Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número {numero}")
except ValueError:
    print("Erro: você não digitou um número inteiro.")


# Exercício 2: Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação - ZeroDivisionError.

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a / b
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
except ValueError:
    print("Erro: você deve digitar números válidos.")


#  Exercício 3: Crie uma função que aceite uma lista e um índice como entrada e retorne o elemento naquele índice. Manipule a exceção caso o índice seja inválido.

def acessar_elemento(lista, indice):
    try:
        print(f"O elemento no índice {indice} é: {lista[indice]}")
    except IndexError:
        print("Erro: índice fora do alcance da lista.")

# Exemplo de uso
lista = [10, 20, 30, 40]
indice = int(input("Digite o índice que deseja acessar: "))
acessar_elemento(lista, indice)


#  Exercício 4: Crie uma função que divida dois números e manipule a exceção caso o divisor seja zero.

def dividir(n1, n2):
    try:
        resultado = n1 / n2
        print(f"Resultado da divisão: {resultado}")
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.")

# Exemplo de uso
a = float(input("Digite o numerador: "))
b = float(input("Digite o denominador: "))
dividir(a, b)
