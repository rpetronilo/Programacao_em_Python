# Sistema de Notas de Alunos

senha_correta = "1234"
tentativas = 0
acesso_liberado = False

# Acesso com até 3 tentativas
while tentativas < 3:
    senha = input("Digite a senha de acesso: ")
    if senha == senha_correta:
        print("Acesso liberado. Bem-vindo ao sistema de notas!")
        acesso_liberado = True
        break
    else:
        tentativas += 1
        print(f"Senha incorreta! Tentativas restantes: {3 - tentativas}")

if not acesso_liberado:
    print("Conta bloqueada por excesso de tentativas.")
else:
    alunos = []

    # Cadastro e notas de 3 alunos
    for a in range(3):
        print(f"\n--- Aluno {a+1} ---")
        nome = input("Nome do aluno: ")
        notas = []

        try:
            num_notas = int(input(f"Quantas notas deseja inserir para {nome}? "))
            i = 0
            while i < num_notas:
                nota = float(input(f"Digite a nota {i+1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    i += 1
                else:
                    print("Nota inválida! Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Erro: entrada inválida! Use apenas números.")

        if len(notas) > 0:
            media = sum(notas) / len(notas)
            if media >= 7:
                situacao = "Aprovado ✅"
            elif media >= 5:
                situacao = "Recuperação ⚠️"
            else:
                situacao = "Reprovado ❌"
        else:
            media = 0
            situacao = "Sem notas válidas ❌"

        # Guardar dados do aluno
        alunos.append({
            "nome": nome,
            "notas": notas,
            "media": media,
            "situacao": situacao
        })

    # Exibir relatório final
    print("\n===== RELATÓRIO FINAL =====")
    for aluno in alunos:
        print(f"\nNome: {aluno['nome']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {aluno['media']:.2f}")
        print(f"Situação: {aluno['situacao']}")
