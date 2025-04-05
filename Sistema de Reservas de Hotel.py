# Sistema de Reservas de Hotel
# Cadastro dos clientes
clientes = []

# Coletando o nome e idade de até 3 clientes
for i in range(3):
    nome = input(f"Digite o nome do cliente {i+1}: ")
    idade = int(input(f"Digite a idade do cliente {i+1}: "))
    clientes.append({'nome': nome, 'idade': idade})

# Preços dos quartos
preco_simples = 100
preco_duplo = 150
preco_luxo = 250

# Cadastro das reservas
reservas = []

for i in range(3):
    print(f"\nCliente {clientes[i]['nome']}, escolha o tipo de quarto:")
    print("1. Simples (R$ 100,00 por dia)")
    print("2. Duplo (R$ 150,00 por dia)")
    print("3. Luxo (R$ 250,00 por dia)")
    
    tipo_quarto = int(input("Digite o número do tipo de quarto escolhido: "))
    dias = int(input(f"Quantos dias {clientes[i]['nome']} ficará no hotel? "))

    # Calculando o valor total da estadia
    if tipo_quarto == 1:
        valor_total = preco_simples * dias
        tipo_quarto_nome = "Simples"
    elif tipo_quarto == 2:
        valor_total = preco_duplo * dias
        tipo_quarto_nome = "Duplo"
    elif tipo_quarto == 3:
        valor_total = preco_luxo * dias
        tipo_quarto_nome = "Luxo"
    else:
        print("Opção inválida! Escolha entre 1, 2 ou 3.")
        valor_total = 0
        tipo_quarto_nome = "Indefinido"

    # Armazenando a reserva
    reservas.append({'cliente': clientes[i]['nome'], 'tipo_quarto': tipo_quarto_nome, 'dias': dias, 'valor_total': valor_total})

# Exibindo o valor total a ser pago por cada cliente
print("\nResumo das Reservas:")
for reserva in reservas:
    print(f"{reserva['cliente']} escolheu o quarto {reserva['tipo_quarto']} e ficará {reserva['dias']} dias.")
    print(f"Valor total a ser pago: R$ {reserva['valor_total']:.2f}\n")
