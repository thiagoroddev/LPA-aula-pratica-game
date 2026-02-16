#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from game.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from game.Level import Level
from game.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        # 1. CARREGAMENTO (Load Content)
        # Instanciamos o menu UMA VEZ. A imagem vai para a RAM agora.
        menu = Menu(self.window)

        #Captura a decisão do usuário
        menu_return = menu.run()

        if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            level = Level(self.window, 'Level1', menu_return)
            level_return = level.run()
        elif menu_return == 'EXIT':
            pygame.quit()
            sys.exit()
        else:
            pass