import pygame
from PIL import Image


pygame.init()
window_width = Image.open('icons/tic_tac_toe_grid.png').width
window_height = Image.open('icons/tic_tac_toe_grid.png').height
icon_width = window_width // 3
icon_height = window_height // 3
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True

def import_icon(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

grid = import_icon('icons/tic_tac_toe_grid.png', [window_width, window_height])
nought = import_icon('icons/tic_tac_toe_o.png', [icon_width, icon_height])
cross = import_icon('icons/tic_tac_toe_x.png', [icon_width, icon_height])

board = [[None for _ in range(3)] for _ in range(3)]

# def player_turn():

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # RENDER YOUR GAME HERE
    screen.blit(grid, (0,0))
    screen.blit(nought, (0, 0))
    screen.blit(cross, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()