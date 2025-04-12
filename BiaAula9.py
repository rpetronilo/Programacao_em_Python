# ## ATIVIDADE 2
# aula 9


# Crie um sistema de notas alunos, com as seguintes operações:
# Utilize While(loop é infinito) ou for(finito) 


# - Acesso a conta com condicionais
# - 3 chances de acessar o sistema
# - Após errar 3 x mensagem que diga que a conta bloqueada 
# - Inserir notas 
# - Fazer a média


notas = {
'Ana':0, 
'Paulo':0, 
'Jessica':0
}


for i in range(1,4):
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    if login == '@julia' and senha == '123456':
        print('Cadastre as notas dos alunos: ')
        notas1 = []
        nomes = []
        for chave,valores in notas.items():
            nomes.append(chave)
            notas1.append(valores)
            # print(nomes, notas1)    
            print('Digite as notas:', chave)              
            nota1 = float(input('Digite a nota1:'))
            nota2 = float(input('Digite a nota2:'))
            nota3 = float(input('Digite a nota3:'))
            notas[chave] = [nota1,nota2,nota3]
            media = sum(notas[chave])/len(notas[chave])
            print(media)
         
          


        else:
            break     
           


         
    else:
        print('Acesso negado')  



i= Input('digite enter para sair:')