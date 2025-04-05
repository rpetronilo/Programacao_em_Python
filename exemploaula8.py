produtos = ['arroz', 'Banana', 'Leite', 'feijao', 'pao']
precos = [1.50, 2.00, 3.20, 2.50, 5.00]


carrinho = []
total = 0

print("Produtos disponíveis:")
print("1. arroz - R$ 1.50")
print("2. Banana - R$ 2.00")
print("3. Leite - R$ 3.20")
print("4. feijãp - R$ 2.50")
print("5. pao - R$ 5.00")


escolha1 = input("Escolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar): ")

if escolha1 == '1':
    carrinho.append(produtos[0])
    total += precos[0]
elif escolha1 == '2':
    carrinho.append(produtos[1])
    total += precos[1]
elif escolha1 == '3':
    carrinho.append(produtos[2])
    total += precos[2]
elif escolha1 == '4':
    carrinho.append(produtos[3])
    total += precos[3]
elif escolha1 == '5':
    carrinho.append(produtos[4])
    total += precos[4]


escolha2 = input("Escolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar): ")

if escolha2 == '1':
    carrinho.append(produtos[0])
    total += precos[0]
elif escolha2 == '2':
    carrinho.append(produtos[1])
    total += precos[1]
elif escolha2 == '3':
    carrinho.append(produtos[2])
    total += precos[2]
elif escolha2 == '4':
    carrinho.append(produtos[3])
    total += precos[3]
elif escolha2 == '5':
    carrinho.append(produtos[4])
    total += precos[4]


escolha3 = input("Escolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar): ")

if escolha3 == '1':
    carrinho.append(produtos[0])
    total += precos[0]
elif escolha3 == '2':
    carrinho.append(produtos[1])
    total += precos[1]
elif escolha3 == '3':
    carrinho.append(produtos[2])
    total += precos[2]
elif escolha3 == '4':
    carrinho.append(produtos[3])
    total += precos[3]
elif escolha3 == '5':
    carrinho.append(produtos[4])
    total += precos[4]


print("\nVocê comprou:")
if len(carrinho) > 0:
    print(carrinho)
    print(f"Total: R$ {total:.2f}")
else:
    print("Nenhum produto comprado.")