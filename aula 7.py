produtos =  ['arroz - 0','bebida - 1','coca - 2']
print('Produtos disponiveis', produtos)
valores =  [10.2,20.0,30.00]
print('Valores R$', valores)

meu_carrinho = []
meu_total = []
escolha1  =  int(input('Digite o id 0-1-2'))
escolha2  =  int(input('Digite o id 0-1-2'))
escolha3  =  int(input('Digite o id 0-1-2'))
escolha4  =  int(input('Digite o id 0-1-2'))

meu_carrinho.append(produtos[escolha1])
meu_total.append(valores[escolha1])
meu_carrinho.append(produtos[escolha2])
meu_total.append(valores[escolha2])
meu_carrinho.append(produtos[escolha3])
meu_total.append(valores[escolha3])
meu_carrinho.append(produtos[escolha4])
meu_total.append(valores[escolha4])

print('Seus produtos são:', meu_carrinho)
print('***' * 21)
total =  sum(meu_total)
print('R$', total)