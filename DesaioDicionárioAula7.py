# ## Desafio 1
# Crie um e-commerce com a estrutura de dicionários.


ecommerce = {
'livros':50.00,
'tablets':150.00,
'fones':20.00 
}




# Produtos:  Livros, tablets e fones de ouvido
# As ações: 
# Comprar()
produto1 = input('Digite seu produto: ')
produto2 = input('Digite seu produto: ')


carrinho = []
valores = []


carrinho += (produto1, produto2)
valores = [ecommerce[produto1], ecommerce[produto2]]


print('Produtos', carrinho)
total = sum(valores)


# mostra o valor da compra
print('R$', total)



# Pagar()
print('''Escolha uma forma de pagamento - pix | CC | CD 
      1 - PIX
      2 - CC
      3 - CD
      ''')
pag = ['','pix', 'CC', 'CD']


escolha_pagamento = int(input('>>')) 


print('Forma de pagamento:', pag[escolha_pagamento])
print('Obrigada Volte Sempre!')