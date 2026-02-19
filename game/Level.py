#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame
from pygame import Surface, Rect, Font

from game.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTIONS, EVENT_ENEMY, COLOR_GREEN, COLOR_BLUE, EVENT_TIMEOUT, \
    TIMEOUT_STEP, SPAW_TIME, TIMEOUT_LEVEL
from game.Enemy import Enemy
from game.EntityFactory import EntityFactory
from game.Entity import Entity
from game.EntityMediator import EntityMediator
from game.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list : list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.player_score = player_score  # Adiciona a pontuação dos jogadores ao nível
        
        # Garante que player_score tem pelo menos 2 elementos
        while len(player_score) < 2:
            player_score.append(0)
        
        # Atribui pontuação ao Player1 (busca por nome para garantir)
        for ent in self.entity_list:
            if ent.name == 'Player1':
                ent.score = player_score[0]
                break

        self.timeout = TIMEOUT_LEVEL # 20 segundos
        self.font = pygame.font.SysFont('Arial', 18)
        if game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
            # Atribui pontuação ao Player2 (busca por nome para garantir)
            for ent in self.entity_list:
                if ent.name == 'Player2':
                    ent.score = player_score[1]
                    break

        pygame.time.set_timer(EVENT_ENEMY, SPAW_TIME)
        # pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # Removido - não mais necessário

    def run(self):
        # Extrai o número do level (Level1 -> 1, Level2 -> 2)
        level_number = self.name.replace('Level', '') # Extrai o número do level
        level_folder = f'level-{level_number}' # Pasta correspondente ao level
        pygame.mixer_music.load(f'./asset/{level_folder}/{self.name}.mp3')
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
                if event.type == EVENT_TIMEOUT:
                    # Não precisa decrementar novamente, já é feito por dt
                    pass
            
            # Verifica se o tempo acabou
            if self.timeout <= 0:
                return True

            # Verificação de Game Over - verifica se ainda há players vivos
            found_player1 = False
            found_player2 = False
            for ent in self.entity_list:
                if ent.name == 'Player1':
                    found_player1 = True
                if ent.name == 'Player2':
                    found_player2 = True 

            # Verifica Game Over baseado no modo de jogo
            if self.game_mode == MENU_OPTIONS[0]:  # 1 Player
                if not found_player1:
                    return "GAME_OVER"
            elif self.game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:  # 2 Players
                if not found_player1 and not found_player2:
                    return "GAME_OVER" 

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