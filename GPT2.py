# Sistema de Notas de Alunos

# Solicita o nome do usuário antes de pedir a senha
usuario = input("Digite seu nome para acessar o sistema: ")
senha_correta = "1234"
tentativas = 0
acesso_liberado = False

# Acesso com até 3 tentativas
while tentativas < 3:
    senha = input(f"Olá {usuario}, digite a senha de acesso: ")
    if senha == senha_correta:
        print(f"Acesso liberado. Bem-vindo, {usuario}!\n")
        acesso_liberado = True
        break
    else:
        tentativas += 1
        print(f"Senha incorreta! Tentativas restantes: {3 - tentativas}")

if not acesso_liberado:
    print(f"Conta bloqueada, {usuario}. Por favor, contate o administrador.")
else:
    alunos = []

    # Cadastro de 3 alunos com 3 notas cada
    for a in range(3):
        print(f"\n--- Cadastro do Aluno {a+1} ---")
        nome = input("Nome do aluno: ")
        notas = []

        for i in range(3):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i+1} de {nome}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida! Digite uma nota entre 0 e 10.")
                except ValueError:
                    print("Erro! Digite um número válido.")

        media = sum(notas) / 3

        if media >= 7:
            situacao = "Aprovado ✅"
        elif media >= 5:
            situacao = "Recuperação ⚠️"
        else:
            situacao = "Reprovado ❌"

        alunos.append({
            "nome": nome,
            "notas": notas,
            "media": media,
            "situacao": situacao
        })

    # Relatório final
    print("\n===== RELATÓRIO FINAL =====")
    for aluno in alunos:
        print(f"\nNome: {aluno['nome']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {aluno['media']:.2f}")
        print(f"Situação: {aluno['situacao']}")

