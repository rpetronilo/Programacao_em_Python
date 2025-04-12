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

# Se acesso foi liberado, continua o sistema
if not acesso_liberado:
    print("Conta bloqueada por excesso de tentativas.")
else:
    notas = []
    try:
        num_notas = int(input("Quantas notas você deseja inserir? "))
        i = 0
        while i < num_notas:
            nota = float(input(f"Digite a nota {i+1}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                i += 1
            else:
                print("Nota inválida! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Erro: Digite apenas números válidos.")

    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print(f"\nNotas inseridas: {notas}")
        print(f"Média final: {media:.2f}")

        if media >= 7:
            print("Situação: Aprovado ✅")
        elif media >= 5:
            print("Situação: Recuperação ⚠️")
        else:
            print("Situação: Reprovado ❌")
    else:
        print("Nenhuma nota válida foi inserida.")

