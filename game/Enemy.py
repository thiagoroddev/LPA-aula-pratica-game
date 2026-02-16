#!/usr/bin/python
# -*- coding: utf-8 -*-

from game.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.Attribute1 = None

    def move(self, ):
        pass
