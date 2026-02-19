#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from game.Const import ENTITY_SPEED, WIN_HEIGHT, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_SHOOT, ENTITY_SHOOT_DELAY, WIN_WIDTH
from game.Entity import Entity
from game.PlayerShoot import PlayerShoot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self, ):
        pressed_keys = pygame.key.get_pressed()

        # Movimento para CIMA (UP)
        if pressed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        # Movimento para BAIXO (DOWN)
        # Verifica se o fundo do player (bottom) é menor que a altura da tela
        if pressed_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        # Movimento para a DIREITA (RIGHT
        if pressed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]


    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[PLAYER_KEY_SHOOT[self.name]]:
               return PlayerShoot(name=f'{self.name}Shoot', position=(self.rect.centerx, self.rect.centery))
            else:
                return None
        return None

    def update(self, ):
        pass