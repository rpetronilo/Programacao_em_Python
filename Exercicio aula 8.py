#1* Verifique se um número é positivo, negativo ou zero

num = float(input("Digite um número: "))
if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")


#2* Verifique se uma pessoa pode votar com base na idade

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")

#3* Determine se um número é par ou ímpar

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


#4* Verifique se um triângulo é equilátero, isósceles ou escaleno

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")


#5* Determine se um número é múltiplo de 5 e 7

numero = int(input("Digite um número: "))

if numero % 5 == 0 and numero % 7 == 0:
    print("O número é múltiplo de 5 e 7.")
else:
    print("O número não é múltiplo de 5 e 7.")


#6* Verifique se um número é positivo e maior que 10

numero = float(input("Digite um número: "))

if numero > 10:
    print("O número é positivo e maior que 10.")
else:
    print("O número não é positivo e maior que 10.")


#7* Verifique se um número é divisível por 3 ou 5

numero = int(input("Digite um número: "))

if numero % 3 == 0 or numero % 5 == 0:
    print("O número é divisível por 3 ou 5.")
else:
    print("O número não é divisível por 3 nem por 5.")