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
    fonte_turno = pygame.font.Font(None, 18)
    fonte_resultado = pygame.font.Font(None, 26)


    nome_jogo = "CAÇA AOS BESOUROS"


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


    pos_jogador1 = (5, 10)
    pos_jogador2 = (350, 10)
    pos_titulo = (105, 5)
    pos_turno = (135, 65)
    pos_footer = (70, 390)


    # botão da tela inicial
    botao_jogar_x = 130
    botao_jogar_y = 300
    botao_jogar_largura = 180
    botao_jogar_altura = 46


    # janela que aparece quando o jogo termina
    painel_x = 80
    painel_y = 135
    painel_largura = 280
    painel_altura = 170


    # botão de reiniciar, dentro da janela de fim de jogo
    botao_reiniciar_x = 120
    botao_reiniciar_y = 239
    botao_reiniciar_largura = 200
    botao_reiniciar_altura = 46


    cor_botao = (76, 128, 67)


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


    pontuacao_jogador1 = 0
    pontuacao_jogador2 = 0
    vez_jogador = 1
    num_celulas_abertas = 0


    jogo = True
    estado_jogo = "menu"


    while jogo:


        for evento in pygame.event.get():


            if (evento.type == pygame.QUIT):
                jogo = False
                break


            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):


                mouse_x, mouse_y = evento.pos


                if (estado_jogo == "menu"):


                    if (
                        mouse_x >= botao_jogar_x
                        and mouse_x <= botao_jogar_x + botao_jogar_largura
                        and mouse_y >= botao_jogar_y
                        and mouse_y <= botao_jogar_y + botao_jogar_altura
                    ):
                        estado_jogo = "jogando"


                elif (estado_jogo == "fim"):


                    if (
                        mouse_x >= botao_reiniciar_x
                        and mouse_x <= botao_reiniciar_x + botao_reiniciar_largura
                        and mouse_y >= botao_reiniciar_y
                        and mouse_y <= botao_reiniciar_y + botao_reiniciar_altura
                    ):


                        # sorteia um tabuleiro novo, do mesmo jeito que no início
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


                        pontuacao_jogador1 = 0
                        pontuacao_jogador2 = 0
                        vez_jogador = 1
                        num_celulas_abertas = 0
                        estado_jogo = "jogando"


                elif (estado_jogo == "jogando"):


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
                            estado_jogo = "fim"
                        else:
                            if (vez_jogador == 1):
                                vez_jogador = 2
                            else:
                                vez_jogador = 1


        tela.blit(
            background,
            (0, 0)
        )


        if (estado_jogo == "menu"):


            titulo_x = (largura_tela - placa_titulo.get_width()) // 2
            titulo_y = 100


            tela.blit(
                placa_titulo,
                (titulo_x, titulo_y)
            )


            texto_nome = fonte.render(nome_jogo, True, cores.branco)


            tela.blit(
                texto_nome,
                (
                    titulo_x + (placa_titulo.get_width() - texto_nome.get_width()) // 2,
                    titulo_y + (placa_titulo.get_height() - texto_nome.get_height()) // 2
                )
            )


            pygame.draw.rect(
                tela,
                cor_botao,
                (botao_jogar_x, botao_jogar_y, botao_jogar_largura, botao_jogar_altura)
            )


            texto_jogar = fonte.render("JOGAR", True, cores.branco)


            tela.blit(
                texto_jogar,
                (
                    botao_jogar_x + (botao_jogar_largura - texto_jogar.get_width()) // 2,
                    botao_jogar_y + (botao_jogar_altura - texto_jogar.get_height()) // 2
                )
            )


            pygame.display.update()
            continue


        tela.blit(
            placa_jogador1,
            pos_jogador1
        )


        tela.blit(
            placa_titulo,
            pos_titulo
        )


        texto_nome = fonte.render(nome_jogo, True, cores.branco)


        tela.blit(
            texto_nome,
            (
                pos_titulo[0] + (placa_titulo.get_width() - texto_nome.get_width()) // 2,
                pos_titulo[1] + (placa_titulo.get_height() - texto_nome.get_height()) // 2
            )
        )


        tela.blit(
            placa_jogador2,
            pos_jogador2
        )


        tela.blit(
            placa_turno,
            pos_turno
        )


        texto_jogador1 = fonte.render(
            nome_jogador1,
            True,
            cores.verde
        )


        tela.blit(
            texto_jogador1,
            (
                pos_jogador1[0] + (placa_jogador1.get_width() - texto_jogador1.get_width()) // 2,
                pos_jogador1[1] + 15
            )
        )


        texto_pontuacao1 = fonte.render(
            str(pontuacao_jogador1),
            True,
            cores.verde
        )


        tela.blit(
            texto_pontuacao1,
            (
                pos_jogador1[0] + (placa_jogador1.get_width() - texto_pontuacao1.get_width()) // 2,
                pos_jogador1[1] + 35
            )
        )


        texto_jogador2 = fonte.render(
            nome_jogador2,
            True,
            cores.rosa
        )


        tela.blit(
            texto_jogador2,
            (
                pos_jogador2[0] + (placa_jogador2.get_width() - texto_jogador2.get_width()) // 2,
                pos_jogador2[1] + 15
            )
        )


        texto_pontuacao2 = fonte.render(
            str(pontuacao_jogador2),
            True,
            cores.rosa
        )


        tela.blit(
            texto_pontuacao2,
            (
                pos_jogador2[0] + (placa_jogador2.get_width() - texto_pontuacao2.get_width()) // 2,
                pos_jogador2[1] + 35
            )
        )


        if (estado_jogo == "fim"):


            texto_turno = fonte_turno.render(
                "FIM DE JOGO",
                True,
                cores.branco
            )


        elif (vez_jogador == 1):


            texto_turno = fonte_turno.render(
                "VEZ DO JOGADOR 1",
                True,
                cores.verde
            )


        else:


            texto_turno = fonte_turno.render(
                "VEZ DO JOGADOR 2",
                True,
                cores.rosa
            )


        tela.blit(
            texto_turno,
            (
                pos_turno[0] + (placa_turno.get_width() - texto_turno.get_width()) // 2,
                pos_turno[1] + (placa_turno.get_height() - texto_turno.get_height()) // 2
            )
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
                            x + (lado_celula - texto.get_width()) // 2,
                            y + (lado_celula - texto.get_height()) // 2
                        )
                    )


        tela.blit(
            placa_footer,
            pos_footer
        )


        texto_footer = fonte.render(
            "ENCONTRE OS BESOUROS!",
            True,
            cores.branco
        )


        tela.blit(
            texto_footer,
            (
                pos_footer[0] + (placa_footer.get_width() - texto_footer.get_width()) // 2,
                pos_footer[1] + (placa_footer.get_height() - texto_footer.get_height()) // 2
            )
        )


        if (estado_jogo == "fim"):


            # escurece o tabuleiro por trás da janela de fim de jogo
            escurecer = pygame.Surface((largura_tela, altura_tela))
            escurecer.set_alpha(150)
            escurecer.fill((0, 0, 0))
            tela.blit(escurecer, (0, 0))


            pygame.draw.rect(
                tela,
                (245, 236, 214),
                (painel_x, painel_y, painel_largura, painel_altura)
            )


            pygame.draw.rect(
                tela,
                cor_botao,
                (painel_x, painel_y, painel_largura, painel_altura),
                3
            )


            texto_fim = fonte.render(
                "FIM DE JOGO",
                True,
                (60, 45, 30)
            )


            tela.blit(
                texto_fim,
                (
                    painel_x + (painel_largura - texto_fim.get_width()) // 2,
                    painel_y + 20
                )
            )


            if (pontuacao_jogador1 > pontuacao_jogador2):
                resultado = "JOGADOR 1 VENCEU!"
            elif (pontuacao_jogador2 > pontuacao_jogador1):
                resultado = "JOGADOR 2 VENCEU!"
            else:
                resultado = "EMPATE!"


            texto_resultado = fonte_resultado.render(
                resultado,
                True,
                (60, 45, 30)
            )


            tela.blit(
                texto_resultado,
                (
                    painel_x + (painel_largura - texto_resultado.get_width()) // 2,
                    painel_y + 55
                )
            )


            pygame.draw.rect(
                tela,
                cor_botao,
                (botao_reiniciar_x, botao_reiniciar_y, botao_reiniciar_largura, botao_reiniciar_altura)
            )


            texto_reiniciar = fonte.render(
                "JOGAR NOVAMENTE",
                True,
                cores.branco
            )


            tela.blit(
                texto_reiniciar,
                (
                    botao_reiniciar_x + (botao_reiniciar_largura - texto_reiniciar.get_width()) // 2,
                    botao_reiniciar_y + (botao_reiniciar_altura - texto_reiniciar.get_height()) // 2
                )
            )


        pygame.display.update()


    pygame.quit()




if __name__ == "__main__":
    main()
