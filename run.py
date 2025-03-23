import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura = 1000
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
preto = (0, 0, 0)

# Tamanho do bloco da cobrinha
tamanho_bloco = 20

# Velocidade da cobrinha
velocidade = 10

# Fonte para texto
fonte = pygame.font.SysFont(None, 30)

# Função para exibir a pontuação
def exibir_pontuacao(pontuacao):
    texto = fonte.render("Pontuação: " + str(pontuacao), True, branco)
    tela.blit(texto, [0, 0])

# Função principal do jogo
def jogo_cobrinha():
    # Posição inicial da cobrinha
    cobrinha_x = largura / 2
    cobrinha_y = altura / 2

    # Mudança na posição da cobrinha
    cobrinha_x_muda = 0
    cobrinha_y_muda = 0

    # Lista para armazenar o corpo da cobrinha
    cobrinha_corpo = []
    comprimento_cobrinha = 1

    # Posição da comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco

    # Loop do jogo
    jogo_fechado = False
    jogo_fim = False

    while not jogo_fechado:
        while jogo_fim == True:
            tela.fill(preto)
            texto = fonte.render("Você perdeu! Pressione C para jogar novamente ou Q para sair.", True, vermelho)
            tela.blit(texto, [largura / 6, altura / 3])
            exibir_pontuacao(comprimento_cobrinha - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        jogo_fechado = True
                        jogo_fim = False
                    if evento.key == pygame.K_c:
                        jogo_cobrinha()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_fechado = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and cobrinha_x_muda == 0:
                    cobrinha_x_muda = -tamanho_bloco
                    cobrinha_y_muda = 0
                elif evento.key == pygame.K_RIGHT and cobrinha_x_muda == 0:
                    cobrinha_x_muda = tamanho_bloco
                    cobrinha_y_muda = 0
                elif evento.key == pygame.K_UP and cobrinha_y_muda == 0:
                    cobrinha_y_muda = -tamanho_bloco
                    cobrinha_x_muda = 0
                elif evento.key == pygame.K_DOWN and cobrinha_y_muda == 0:
                    cobrinha_y_muda = tamanho_bloco
                    cobrinha_x_muda = 0

        if cobrinha_x >= largura or cobrinha_x < 0 or cobrinha_y >= altura or cobrinha_y < 0:
            jogo_fim = True

        cobrinha_x += cobrinha_x_muda
        cobrinha_y += cobrinha_y_muda

        tela.fill(preto)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cobrinha_cabeca = []
        cobrinha_cabeca.append(cobrinha_x)
        cobrinha_cabeca.append(cobrinha_y)
        cobrinha_corpo.append(cobrinha_cabeca)

        if len(cobrinha_corpo) > comprimento_cobrinha:
            del cobrinha_corpo[0]

        for segmento in cobrinha_corpo[:-1]:
            if segmento == cobrinha_cabeca:
                jogo_fim = True

        for segmento in cobrinha_corpo:
            pygame.draw.rect(tela, verde, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])

        exibir_pontuacao(comprimento_cobrinha - 1)
        pygame.display.update()

        if cobrinha_x == comida_x and cobrinha_y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
            comprimento_cobrinha += 1

        pygame.time.Clock().tick(velocidade)

    pygame.quit()
    quit()

jogo_cobrinha()