import pygame as pg
print('Setup initialization')
pg.init()
window = pg.display.set_mode((800, 600)) # size of the window
print('Setup complete')
pg.display.set_caption('My Game')

print('Loop Start')
while True:
    #Check for all eventes
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() # end game