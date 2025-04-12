# Sistema de Notas Simplificado

# Usuários e senhas cadastrados (pode ser uma base inicial)
usuarios_senhas = {
    "professor1": "1234",
    "professor2": "abcd",
    "admin": "admin123"
}

# Função para login
def fazer_login():
    usuario = input("Nome de usuário: ")

    # Verifica se o usuário existe no dicionário
    if usuario not in usuarios_senhas:
        print("Usuário não encontrado.")
        criar_usuario = input("Deseja criar uma nova conta? (s/n): ")
        if criar_usuario.lower() == 's':
            senha = input("Digite a senha para o novo usuário: ")
            usuarios_senhas[usuario] = senha
            print(f"Usuário {usuario} criado com sucesso!\n")
            return usuario, senha
        else:
            print("Encerrando o programa.")
            exit()
    else:
        for i in range(3):
            senha = input(f"Olá {usuario}, digite a senha: ")
            if senha == usuarios_senhas[usuario]:
                print(f"Acesso liberado, {usuario}!\n")
                return usuario, senha
            print(f"Senha incorreta! Tentativas restantes: {2 - i}")
        else:
            print("Conta bloqueada. Contate o administrador.")
            exit()

# Realiza o login
usuario, senha = fazer_login()

# Cadastro de alunos
alunos = []
for a in range(1, 4):
    nome = input(f"\nAluno {a} - Nome: ")
    notas = [float(input(f"Nota {i+1}: ")) for i in range(3)]
    while any(n < 0 or n > 10 for n in notas):
        print("Notas inválidas! Digite novamente.")
        notas = [float(input(f"Nota {i+1}: ")) for i in range(3)]
    media = sum(notas)/3
    situacao = "Aprovado ✅" if media >= 7 else "Recuperação ⚠️" if media >= 5 else "Reprovado ❌"
    alunos.append((nome, notas, media, situacao))

# Relatório
print("\n===== RELATÓRIO FINAL =====")
for nome, notas, media, situacao in alunos:
    print(f"\nNome: {nome}\nNotas: {[f'{n:.1f}' for n in notas]}\nMédia: {media:.2f}\nSituação: {situacao}")

