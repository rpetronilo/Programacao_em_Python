# input() print() variáveis  + - * / | > < >= <= !=

# sistema de notas de escola / média 

print('sistema de notas de escola')

nome1 = input('Digite o nome do aluno 1')

nota1 = float(input('nota 1'))
nota2 = float(input('nota 2'))
nota3 = float(input('nota 3'))
nota4 = float(input('nota 4'))
nota5 = float(input('nota 5'))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

print('Aluno:')
print(nome1)
print(media)

if media >= 7.0 : situacao = 'aprovado'
elif media >=5.0: situacao = 'Recuperação'
elif media <5.0: situacao = 'reprovado'

print('Aluno' , nome1)
print('Situação',situacao)
