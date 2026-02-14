#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
import sys #Necessário para fechar o game corretamente

from pygame import Surface, Font

from game.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTIONS, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        # O .convert() é crucial! Ele converte o formato de pixel da imagem
        # para o mesmo da tela, tornando o desenho muito mais rápido.
        self.surf = pygame.image.load('./asset/Menu.jpg').convert()
        self.rect = self.surf.get_rect(left = 0, top = 0)

        #Carrega a música(apenas carrega, não toca)
        # Nota: mixer.music é para streaming (arquivos longos).
        # Para sons curtos (tiros, pulos), usa-se pygame.Sound.
        pygame.mixer_music.load('asset/Music.mp3')


    def run(self,):
        # 1. Inicia a música em loop (-1 significa loop infinito)
        pygame.mixer_music.play(-1)

        #Loop específico do Menu
        while True:
            # Apenas desenha a imagem carregada na memória
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(text_size=150, text="Mountain", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH /2), 170))
            self.menu_text(text_size=130, text="Shooter", text_color=COLOR_ORANGE,
                           text_center_pos=((WIN_WIDTH / 2), 300))

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(text_size=30,text=MENU_OPTIONS[i], text_color=COLOR_WHITE,
                           text_center_pos=((WIN_WIDTH / 2), 400 + 30 * i))

            # Atualiza a tela inteira
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'EXIT' #Avisa ao Game que é para fechar tudo

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer_music.stop()
                        return 'START' #Avisa ao Game que é para jogar






    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont('Arial', size=text_size)
        text_surt: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surt.get_rect(center = text_center_pos)
        self.window.blit(source=text_surt,dest=text_rect)