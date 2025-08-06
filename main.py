import pygame
from PIL import Image


pygame.init()
window_width = Image.open('icons/TicTacToeG.png').width
window_height = Image.open('icons/TicTacToeG.png').height
icon_width = window_width // 3
icon_height = window_height // 3
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True

def import_icon(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

grid = import_icon('icons/TicTacToeG.png', [window_width, window_height])
nought = import_icon('icons/TicTacToeO.png', [icon_width, icon_height])
cross = import_icon('icons/TicTacToeX.png', [icon_width, icon_height])
player = 1


board = [[None for _ in range(3)] for _ in range(3)]

def player_turn(current_player):
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        mouse_x_position = pygame.mouse.get_pos()[0] // icon_width
        mouse_y_position = pygame.mouse.get_pos()[1] // icon_height
        if board[mouse_x_position][mouse_y_position] is None:
            board[mouse_x_position][mouse_y_position] = current_player
            global player
            if player == 1:
                player = 2
            else:
                player = 1

def render_icons():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                screen.blit(nought, (row * icon_width, col * icon_height))
            if board[row][col] == 2:
                screen.blit(cross, (row * icon_width, col * icon_height))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE

    pygame.display.flip()
    screen.fill("white")
    screen.blit(grid, (0, 0))
    player_turn(player)
    render_icons()
    clock.tick(60)

pygame.quit()