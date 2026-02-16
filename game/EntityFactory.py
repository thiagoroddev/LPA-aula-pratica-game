#!/usr/bin/python
# -*- coding: utf-8 -*-

from game.Background import Background
from game.Const import WIN_WIDTH


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}.png',(0,0)))
                    list_bg.append(Background(f'Level1Bg{i}.png', (WIN_WIDTH, 0)))
                return list_bg
            case _:
                return None

