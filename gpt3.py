# Sistema de Notas de Alunos (versão simplificada)

# Login
usuario = input("Digite seu nome para acessar o sistema: ")
for tentativa in range(3):
    senha = input(f"Olá {usuario}, digite a senha de acesso: ")
    if senha == "1234":
        print(f"Acesso liberado. Bem-vindo, {usuario}!\n")
        break
    else:
        print(f"Senha incorreta! Tentativas restantes: {2 - tentativa}")
else:
    print(f"Conta bloqueada, {usuario}. Por favor, contate o administrador.")
    exit()

# Cadastro de alunos
alunos = []
for a in range(1, 4):
    nome = input(f"\nNome do Aluno {a}: ")
    notas = []

    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Nota {i} de {nome}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota fora do intervalo (0-10).")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    media = sum(notas) / 3
    situacao = "Aprovado ✅" if media >= 7 else "Recuperação ⚠️" if media >= 5 else "Reprovado ❌"

    alunos.append({"nome": nome, "notas": notas, "media": media, "situacao": situacao})

# Relatório final
print("\n===== RELATÓRIO FINAL =====")
for aluno in alunos:
    print(f"\nNome: {aluno['nome']}")
    print(f"Notas: {[f'{n:.2f}' for n in aluno['notas']]}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")
