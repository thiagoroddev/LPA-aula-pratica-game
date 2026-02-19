#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from pygame.key import name

from game.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from game.Level import Level
from game.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        # Loop principal do jogo - sempre volta ao menu
        while True:
            # 1. CARREGAMENTO (Load Content)
            # Instanciamos o menu UMA VEZ. A imagem vai para a RAM agora.
            menu = Menu(self.window)

            #Captura a decisão do usuário
            menu_return = menu.run()

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                player_score = [0, 0]  # Inicializa as pontuações dos jogadores (Player1, Player2)
                
                # Level 1
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run()
                
                if level_return == "EXIT":
                    pygame.quit()
                    sys.exit()
                elif level_return == "GAME_OVER":
                    # Player(s) morreu(ram), volta ao menu
                    continue
                elif level_return:  # Level 1 completado com sucesso
                    # Atualiza pontuação para o próximo level
                    for ent in level.entity_list:
                        if ent.name == 'Player1':
                            player_score[0] = ent.score
                        elif ent.name == 'Player2':
                            player_score[1] = ent.score
                    
                    # Level 2
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run()
                    
                    if level_return == "EXIT":
                        pygame.quit()
                        sys.exit()
                    elif level_return == "GAME_OVER":
                        # Player(s) morreu(ram), volta ao menu
                        continue
                    # Se completou Level 2 (level_return == True), volta ao menu (continua o loop)

            elif menu_return == 'EXIT':
                pygame.quit()
                sys.exit()
            else:
                pass