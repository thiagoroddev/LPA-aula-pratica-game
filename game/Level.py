#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame
from pygame import Surface, Rect, Font

from game.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTIONS, EVENT_ENEMY, COLOR_GREEN, COLOR_BLUE
from game.Enemy import Enemy
from game.EntityFactory import EntityFactory
from game.Entity import Entity
from game.EntityMediator import EntityMediator
from game.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list : list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000 # 20 segundos
        self.font = pygame.font.SysFont('Arial', 18)
        if game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 2000)

    def run(self):
        pygame.mixer_music.load(f'./asset/level-1/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock() #Controla FPS

        while True:

            dt = clock.tick(60)
            self.timeout -= dt

            #Checa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "EXIT"
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))



            # Atualização
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.leve_text(f'Player1 - Health: {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 30))
                if ent.name == 'Player2':
                    self.leve_text(f'Player2 - Health: {ent.health} | Score: {ent.score}', COLOR_BLUE, (10, 60))


            # printed text
            self.leve_text(f'{self.name} - Timeout:  {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.leve_text(f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 25))
            self.leve_text(f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT -55))
            # Desenho
            pygame.display.flip()
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)


    def leve_text(self, text:str, text_color:tuple, text_pos: tuple):

        text_surface: Surface = self.font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surface,dest=text_rect)