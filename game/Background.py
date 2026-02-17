#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from game.Entity import Entity
from game.Const import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT


class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        #Redimensiona as imagens do level para o tamannho da janela
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))

        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

