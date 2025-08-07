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
font = pygame.font.Font('freesansbold.ttf', 48)
text = font.render('', True, 'red')
text_rect = text.get_rect(center=(window_width // 2, window_height // 2))

def import_icon(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

grid = import_icon('icons/TicTacToeG.png', [window_width, window_height])
nought = import_icon('icons/TicTacToeO.png', [icon_width, icon_height])
cross = import_icon('icons/TicTacToeX.png', [icon_width, icon_height])
player = 1
game_over = False

board = [[None for _ in range(3)] for _ in range(3)]

def player_turn(current_player):
    if not game_over and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        mouse_x_position = pygame.mouse.get_pos()[0] // icon_width
        mouse_y_position = pygame.mouse.get_pos()[1] // icon_height
        if board[mouse_y_position][mouse_x_position] is None:
            board[mouse_y_position][mouse_x_position] = current_player
            global player
            player = 2 if player == 1 else 1

def render_icons():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                screen.blit(nought, (col * icon_width, row * icon_height))
            if board[row][col] == 2:
                screen.blit(cross, (col * icon_width, row * icon_height))

def check_rows(current_player):
    for row in board:
        if row[0] == row[1] == row[2] == current_player:
            return True
    return False

def check_columns(current_player):
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == current_player:
            return True
    return False

def check_diagonals(current_player):
    if board[0][0] == board[1][1] == board[2][2] == current_player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == current_player:
        return True
    return False

def check_win(current_player):
    global text
    if check_rows(current_player) or check_columns(current_player) or check_diagonals(current_player):
        if current_player == 1:
            text = font.render('Noughts win!', True, (0, 100, 0))
        if current_player == 2:
            text = font.render('Crosses win!', True, (0, 100, 0))
        return True
    return False

def check_draw():
    global text
    for row in board:
        for col in row:
            if col is None:
                return False
    text = font.render("It's a draw!", True, (0, 100, 0))
    return True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE

    pygame.display.flip()
    screen.fill("white")
    screen.blit(grid, (0, 0))
    player_to_check = player
    player_turn(player)
    render_icons()
    if check_win(player_to_check) or check_draw():
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
        game_over = True
    if game_over:
        screen.blit(text, text_rect)
    clock.tick(60)

pygame.quit()