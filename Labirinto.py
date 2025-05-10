# Importa o módulo pygame que contém funções para criação de jogos e manipulação de gráficos
import pygame

# Inicializa todos os módulos do Pygame (necessário para começar a usar o Pygame)
pygame.init()

# Definição das dimensões da tela do jogo (largura e altura)
largura, altura = 400, 400

# Criação da janela do jogo com as dimensões definidas
tela = pygame.display.set_mode((largura, altura))

# Define o título da janela do jogo
pygame.display.set_caption("Labirinto")

# Definição das cores que serão usadas no jogo
preto = (0, 0, 0)  # Cor preta (R, G, B)
branco = (255, 255, 255)  # Cor branca
vermelho = (255, 0, 0)  # Cor vermelha

# Define o tamanho de cada célula no labirinto (em pixels)
tamanho_celula = 40

# Representação do labirinto. 1 = parede, 0 = caminho livre.
# A matriz tem 10x10 células.
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Definição da posição inicial do jogador (em coordenadas de pixels)
x, y = 1 * tamanho_celula, 1 * tamanho_celula  # Inicia o jogador na célula (1, 1)
velocidade = 40  # Define a velocidade do movimento do jogador (em pixels por frame)

# Função para desenhar o labirinto na tela
def desenhar_labirinto():
    # Percorre todas as linhas e colunas da matriz labirinto
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            # Verifica se é parede (1) ou caminho livre (0)
            cor = preto if labirinto[linha][coluna] == 1 else branco
            # Desenha o retângulo correspondente à célula na tela
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# Loop principal do jogo
executando = True  # Define se o jogo deve continuar ou não
while executando:
    # Processa os eventos do jogo (como o fechamento da janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Se o evento for o fechamento da janela
            executando = False  # Finaliza o loop e encerra o jogo

    # Obtém o estado das teclas pressionadas no momento
    teclas = pygame.key.get_pressed()
    
    # Movimento do jogador para a esquerda (tecla de seta esquerda)
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade  # Calcula a nova posição horizontal (x) do jogador
        # Verifica se a célula à esquerda está livre (0) para mover
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x  # Atualiza a posição do jogador

    # Movimento do jogador para a direita (tecla de seta direita)
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade  # Calcula a nova posição horizontal (x) do jogador
        # Verifica se a célula à direita está livre (0) para mover
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x  # Atualiza a posição do jogador

    # Movimento do jogador para cima (tecla de seta para cima)
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade  # Calcula a nova posição vertical (y) do jogador
        # Verifica se a célula acima está livre (0) para mover
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y  # Atualiza a posição do jogador

    # Movimento do jogador para baixo (tecla de seta para baixo)
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade  # Calcula a nova posição vertical (y) do jogador
        # Verifica se a célula abaixo está livre (0) para mover
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y  # Atualiza a posição do jogador

    # Preenche a tela com a cor branca antes de desenhar novamente
    tela.fill(branco)

    # Desenha o labirinto na tela
    desenhar_labirinto()

    # Desenha o jogador na tela com a cor vermelha
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    # Atualiza a tela para refletir as mudanças feitas
    pygame.display.flip()

    # Controla a taxa de atualização da tela (10 quadros por segundo)
    pygame.time.Clock().tick(10)

# Encerra o Pygame após o loop principal
pygame.quit()
