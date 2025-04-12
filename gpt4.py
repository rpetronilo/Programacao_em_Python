# Sistema de Notas Simplificado

# Login com 3 tentativas
usuario = input("Nome de usuário: ")
for i in range(3):
    if input(f"Olá {usuario}, digite a senha: ") == "1234":
        print(f"Acesso liberado, {usuario}!\n")
        break
    print(f"Senha incorreta! Tentativas restantes: {2 - i}")
else:
    print("Conta bloqueada. Contate o administrador.")
    exit()

# Cadastro de alunos
alunos = []
for a in range(1, 4):
    nome = input(f"\nAluno {a} - Nome: ")
    notas = [float(input(f"Nota {i+1}: ")) for i in range(3) if not print(" ", end="")]
    while any(n < 0 or n > 10 for n in notas):
        print("Notas inválidas! Digite novamente.")
        notas = [float(input(f"Nota {i+1}: ")) for i in range(3) if not print(" ", end="")]
    media = sum(notas)/3
    situacao = "Aprovado ✅" if media >= 7 else "Recuperação ⚠️" if media >= 5 else "Reprovado ❌"
    alunos.append((nome, notas, media, situacao))

# Relatório
print("\n===== RELATÓRIO FINAL =====")
for nome, notas, media, situacao in alunos:
    print(f"\nNome: {nome}\nNotas: {[f'{n:.1f}' for n in notas]}\nMédia: {media:.2f}\nSituação: {situacao}")
