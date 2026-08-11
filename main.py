import pygame
import random
import cores


def main():

    pygame.init()

    largura_tela = 440
    altura_tela = 440

    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Caça ao Besouro")

    fonte = pygame.font.Font(None, 20)

    background = pygame.image.load(
        "assets/background.png"
    ).convert()

    placa_titulo = pygame.image.load(
        "assets/placa_titulo.png"
    ).convert_alpha()

    placa_jogador1 = pygame.image.load(
        "assets/placa_placar_jogador_1.png"
    ).convert_alpha()

    placa_jogador2 = pygame.image.load(
        "assets/placa_placar_jogador_2.png"
    ).convert_alpha()

    placa_turno = pygame.image.load(
        "assets/placa_turno.png"
    ).convert_alpha()

    placa_footer = pygame.image.load(
        "assets/placa_footer.png"
    ).convert_alpha()

    casa_fechada = pygame.image.load(
        "assets/casa_fechada.png"
    ).convert_alpha()

    besouro = pygame.image.load(
        "assets/besouro.png"
    ).convert_alpha()

    aranha = pygame.image.load(
        "assets/aranha.png"
    ).convert_alpha()

    background = pygame.transform.scale(
        background,
        (440, 440)
    )

    largura = 230
    altura = int(
        placa_titulo.get_height()
        * largura
        / placa_titulo.get_width()
    )

    placa_titulo = pygame.transform.scale(
        placa_titulo,
        (largura, altura)
    )

    largura = 85
    altura = int(
        placa_jogador1.get_height()
        * largura
        / placa_jogador1.get_width()
    )

    placa_jogador1 = pygame.transform.scale(
        placa_jogador1,
        (largura, altura)
    )

    largura = 85
    altura = int(
        placa_jogador2.get_height()
        * largura
        / placa_jogador2.get_width()
    )

    placa_jogador2 = pygame.transform.scale(
        placa_jogador2,
        (largura, altura)
    )

    largura = 170
    altura = int(
        placa_turno.get_height()
        * largura
        / placa_turno.get_width()
    )

    placa_turno = pygame.transform.scale(
        placa_turno,
        (largura, altura)
    )

    largura = 300
    altura = int(
        placa_footer.get_height()
        * largura
        / placa_footer.get_width()
    )

    placa_footer = pygame.transform.scale(
        placa_footer,
        (largura, altura)
    )

    largura = 75
    altura = int(
        casa_fechada.get_height()
        * largura
        / casa_fechada.get_width()
    )

    casa_fechada = pygame.transform.scale(
        casa_fechada,
        (largura, altura)
    )

    largura = 45
    altura = int(
        besouro.get_height()
        * largura
        / besouro.get_width()
    )

    besouro = pygame.transform.scale(
        besouro,
        (largura, altura)
    )

    largura = 45
    altura = int(
        aranha.get_height()
        * largura
        / aranha.get_width()
    )

    aranha = pygame.transform.scale(
        aranha,
        (largura, altura)
    )

    lado_celula = 75

    inicio_x = 65
    inicio_y = 110

    num_linhas = 4
    num_colunas = 4

    nome_jogador1 = "JOGADOR 1"
    nome_jogador2 = "JOGADOR 2"

    pontuacao_jogador1 = 0
    pontuacao_jogador2 = 0

    conteudo_celula = [
        [None for j in range(num_colunas)]
        for i in range(num_linhas)
    ]

    num_besouros = 0

    while (num_besouros < 6):
        i = random.randint(0, num_linhas - 1)
        j = random.randint(0, num_colunas - 1)

        if (conteudo_celula[i][j] == None):
            conteudo_celula[i][j] = "B"
            num_besouros += 1

    num_aranhas = 0

    while (num_aranhas < 3):
        i = random.randint(0, num_linhas - 1)
        j = random.randint(0, num_colunas - 1)

        if (conteudo_celula[i][j] == None):
            conteudo_celula[i][j] = "A"
            num_aranhas += 1

    for i in range(num_linhas):

        for j in range(num_colunas):

            if (conteudo_celula[i][j] == None):

                num_vizinhos = 0

                if (i > 0 and conteudo_celula[i - 1][j] == "B"):
                    num_vizinhos += 1

                if (i < num_linhas - 1 and conteudo_celula[i + 1][j] == "B"):
                    num_vizinhos += 1

                if (j > 0 and conteudo_celula[i][j - 1] == "B"):
                    num_vizinhos += 1

                if (j < num_colunas - 1 and conteudo_celula[i][j + 1] == "B"):
                    num_vizinhos += 1

                conteudo_celula[i][j] = str(num_vizinhos)

    celula_revelada = [
        [False for i in range(num_colunas)]
        for j in range(num_linhas)
    ]

    jogo = True
    jogo_terminado = False
    vez_jogador = 1
    num_celulas_abertas = 0

    while jogo:

        for evento in pygame.event.get():

            if (evento.type == pygame.QUIT):
                jogo = False
                break

            if (jogo_terminado):
                continue

            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):

                mouse_x, mouse_y = evento.pos

                if (
                    mouse_x < inicio_x
                    or mouse_x >= inicio_x + num_colunas * lado_celula
                    or mouse_y < inicio_y
                    or mouse_y >= inicio_y + num_linhas * lado_celula
                ):
                    continue

                celula_x = (mouse_x - inicio_x) // lado_celula
                celula_y = (mouse_y - inicio_y) // lado_celula

                if (not celula_revelada[celula_y][celula_x]):

                    celula_revelada[celula_y][celula_x] = True
                    num_celulas_abertas += 1

                    if (conteudo_celula[celula_y][celula_x] == "B"):

                        if (vez_jogador == 1):
                            pontuacao_jogador1 += 100
                        else:
                            pontuacao_jogador2 += 100

                    elif (conteudo_celula[celula_y][celula_x] == "A"):

                        if (vez_jogador == 1):
                            pontuacao_jogador1 = max(
                                0,
                                pontuacao_jogador1 - 50
                            )
                        else:
                            pontuacao_jogador2 = max(
                                0,
                                pontuacao_jogador2 - 50
                            )

                    if (num_celulas_abertas == num_linhas * num_colunas):
                        jogo_terminado = True
                    else:
                        if (vez_jogador == 1):
                            vez_jogador = 2
                        else:
                            vez_jogador = 1

        tela.blit(
            background,
            (0, 0)
        )

        tela.blit(
            placa_jogador1,
            (5, 10)
        )

        tela.blit(
            placa_titulo,
            (105, 5)
        )

        tela.blit(
            placa_jogador2,
            (350, 10)
        )

        tela.blit(
            placa_turno,
            (135, 65)
        )

        texto_jogador1 = fonte.render(
            nome_jogador1,
            True,
            cores.verde
        )

        tela.blit(
            texto_jogador1,
            (15, 15)
        )

        texto_pontuacao1 = fonte.render(
            str(pontuacao_jogador1),
            True,
            cores.verde
        )

        tela.blit(
            texto_pontuacao1,
            (35, 35)
        )

        texto_jogador2 = fonte.render(
            nome_jogador2,
            True,
            cores.rosa
        )

        tela.blit(
            texto_jogador2,
            (360, 15)
        )

        texto_pontuacao2 = fonte.render(
            str(pontuacao_jogador2),
            True,
            cores.rosa
        )

        tela.blit(
            texto_pontuacao2,
            (380, 35)
        )

        if (jogo_terminado):

            texto_turno = fonte.render(
                "FIM DE JOGO",
                True,
                cores.branco
            )

        elif (vez_jogador == 1):

            texto_turno = fonte.render(
                "VEZ DO JOGADOR 1",
                True,
                cores.verde
            )

        else:

            texto_turno = fonte.render(
                "VEZ DO JOGADOR 2",
                True,
                cores.rosa
            )

        tela.blit(
            texto_turno,
            (150, 73)
        )

        for linha in range(num_linhas):

            for coluna in range(num_colunas):

                x = inicio_x + coluna * lado_celula
                y = inicio_y + linha * lado_celula

                if (not celula_revelada[linha][coluna]):

                    tela.blit(
                        casa_fechada,
                        (x, y)
                    )

                elif (conteudo_celula[linha][coluna] == "B"):

                    tela.blit(
                        besouro,
                        (
                            x + (lado_celula - besouro.get_width()) // 2,
                            y + (lado_celula - besouro.get_height()) // 2
                        )
                    )

                elif (conteudo_celula[linha][coluna] == "A"):

                    tela.blit(
                        aranha,
                        (
                            x + (lado_celula - aranha.get_width()) // 2,
                            y + (lado_celula - aranha.get_height()) // 2
                        )
                    )

                else:

                    texto = fonte.render(
                        conteudo_celula[linha][coluna],
                        True,
                        cores.preto
                    )

                    tela.blit(
                        texto,
                        (
                            x + 0.4 * lado_celula,
                            y + 0.4 * lado_celula
                        )
                    )

        tela.blit(
            placa_footer,
            (70, 390)
        )

        if (jogo_terminado):

            if (pontuacao_jogador1 > pontuacao_jogador2):
                texto_footer = fonte.render(
                    "JOGADOR 1 VENCEU!",
                    True,
                    cores.branco
                )

            elif (pontuacao_jogador2 > pontuacao_jogador1):
                texto_footer = fonte.render(
                    "JOGADOR 2 VENCEU!",
                    True,
                    cores.branco
                )

            else:
                texto_footer = fonte.render(
                    "EMPATE!",
                    True,
                    cores.branco
                )

        else:

            texto_footer = fonte.render(
                "ENCONTRE OS BESOUROS!",
                True,
                cores.branco
            )

        tela.blit(
            texto_footer,
            (120, 400)
        )

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()