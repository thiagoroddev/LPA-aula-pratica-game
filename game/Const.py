import pygame

COLOR_ORANGE = (255,0,0)
COLOR_WHITE = (255,255,255)
COLOR_YELLOW = (255,255,0)
COLOR_GREEN = (0,255,0)
COLOR_BLUE = (0,0,255)


MENU_OPTIONS = ('NEW GAME 1P',
                'NEW GAME 2P - COOPERATIVE',
                 'NEW GAME 2P - COMPETITIVE',
                 'SCORE',
                 'EXIT')

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'level-1/Level1Bg0': 0,
    'level-1/Level1Bg1': 1,
    'level-1/Level1Bg2': 2,
    'level-1/Level1Bg3': 3,
    'level-1/Level1Bg4': 4,
    'level-1/Level1Bg5': 5,
    'level-1/Level1Bg6': 6,
    'Player1': 3,
    'Player1Shoot': 6,
    'Player2Shoot': 6,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 2,
    'Enemy1Shoot': 3,
    'Enemy2Shoot': 3
}

ENTITY_SCORE = {
    'level-1/Level1Bg0': 0,
    'level-1/Level1Bg1': 0,
    'level-1/Level1Bg2': 0,
    'level-1/Level1Bg3': 0,
    'level-1/Level1Bg4': 0,
    'level-1/Level1Bg5': 0,
    'level-1/Level1Bg6': 0,
    'Player1': 0,
    'Player1Shoot': 0,
    'Player2Shoot': 0,
    'Player2': 0,
    'Enemy1': 100,
    'Enemy2': 110,
    'Enemy1Shoot': 0,
    'Enemy2Shoot': 0
}


PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_LCTRL, 'Player2': pygame.K_RCTRL}

ENTITY_HEALTH = {
    'level-1/Level1Bg0': 999,
    'level-1/Level1Bg1': 999,
    'level-1/Level1Bg2': 999,
    'level-1/Level1Bg3': 999,
    'level-1/Level1Bg4': 999,
    'level-1/Level1Bg5': 999,
    'level-1/Level1Bg6': 999,
    'Player1': 300,
    'Player1Shoot': 1,
    'Player2': 300,
    'Player2Shoot': 1,
    'Enemy1': 50,
    'Enemy2': 50,
    'Enemy1Shoot': 1,
    'Enemy2Shoot': 1

}

ENTITY_SHOOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 20,
    'Enemy2': 20
}

ENTITY_DAMAGE = {
    'level-1/Level1Bg0': 0,
    'level-1/Level1Bg1': 0,
    'level-1/Level1Bg2': 0,
    'level-1/Level1Bg3': 0,
    'level-1/Level1Bg4': 0,
    'level-1/Level1Bg5': 0 ,
    'level-1/Level1Bg6': 0,
    'Player1': 1,
    'Player1Shoot': 25,
    'Player2': 1,
    'Player2Shoot': 20,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy1Shoot': 20,
    'Enemy2Shoot': 20
}

WIN_WIDTH = 1366
WIN_HEIGHT = 768