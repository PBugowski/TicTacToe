"""
Tic Tac Toe Game (Pygame)

This script implements a simple Tic Tac Toe game using Pygame.
Players alternate between placing 'noughts' (O) and 'crosses' (X) on a 3x3 grid.
The game detects wins (rows, columns, diagonals) and draws.

Assets:
    - icons/TicTacToeG.png : Grid image
    - icons/TicTacToeO.png : Nought icon
    - icons/TicTacToeX.png : Cross icon
"""

import pygame
from PIL import Image # Used to get image dimensions before loading into Pygame

# -----------------------
# INITIAL SETUP & CONFIG
# -----------------------
pygame.init()

# Load grid dimensions from image file
GRID_IMAGE_PATH = 'icons/TicTacToeG.png'
window_width = Image.open(GRID_IMAGE_PATH).width
window_height = Image.open(GRID_IMAGE_PATH).height

# Tile size based on grid
tile_width = window_width // 3
tile_height = window_height // 3

# Pygame window setup
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# Fonts & text rendering
font = pygame.font.Font('freesansbold.ttf', 48)
text = font.render('', True, (0, 100, 0))
text_rect = text.get_rect(center=(window_width // 2, window_height // 2))

# Game state
player = 1 # 1 = Noughts, 2 = Crosses
game_over = False
running = True
board = [[None for _ in range(3)] for _ in range(3)] # 3x3 game board

# -----------------------
# HELPER FUNCTIONS
# -----------------------
def import_icon(path: str, resolution: tuple) -> pygame.Surface:
    """
    Load an image from file and scale it to the given resolution.
    """
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)


# Load assets
grid = import_icon(GRID_IMAGE_PATH, (window_width, window_height))
nought = import_icon('icons/TicTacToeO.png', (tile_width, tile_height))
cross = import_icon('icons/TicTacToeX.png', (tile_width, tile_height))


def player_turn(current_player: int):
    """
    Handle a player's turn by placing their icon on the board when they click an empty cell.
    """
    global player
    if not game_over and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        mouse_x_position = pygame.mouse.get_pos()[0] // tile_width
        mouse_y_position = pygame.mouse.get_pos()[1] // tile_height
        if board[mouse_y_position][mouse_x_position] is None:
            board[mouse_y_position][mouse_x_position] = current_player
            player = 2 if player == 1 else 1


def render_icons():
    """
    Draw noughts and crosses on the screen according to the current board state.
    """
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                screen.blit(nought, (col * tile_width, row * tile_height))
            if board[row][col] == 2:
                screen.blit(cross, (col * tile_width, row * tile_height))


def check_rows(current_player: int) -> bool:
    """
    Check if the current player has a complete row.
    """
    for row in board:
        if row[0] == row[1] == row[2] == current_player:
            return True
    return False


def check_columns(current_player: int) -> bool:
    """
    Check if the current player has a complete column.
    """
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == current_player:
            return True
    return False


def check_diagonals(current_player: int) -> bool:
    """
    Check if the current player has a complete diagonal.
    """
    if board[0][0] == board[1][1] == board[2][2] == current_player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == current_player:
        return True
    return False


def check_win(current_player: int) -> bool:
    """
    Check if the current player has won the game and update the display text.
    """
    global text
    if check_rows(current_player) or check_columns(current_player) or check_diagonals(current_player):
        if current_player == 1:
            text = font.render('Noughts win!', True, (0, 100, 0))
        if current_player == 2:
            text = font.render('Crosses win!', True, (0, 100, 0))
        return True
    return False


def check_draw() -> bool:
    """
    Check if the board is full without a winner and update the display text.
    """
    global text
    for row in board:
        for col in row:
            if col is None:
                return False
    text = font.render("It's a draw!", True, (0, 100, 0))
    return True


# -----------------------
# MAIN GAME LOOP
# -----------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background and grid
    screen.fill("white")
    screen.blit(grid, (0, 0))

    # Player turn
    player_to_check = player
    player_turn(player)

    # Draw player icons
    render_icons()

    # Game state checks
    if check_win(player_to_check) or check_draw():
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
        game_over = True

    # Display win/draw message if game is over
    if game_over:
        screen.blit(text, text_rect)

    # Update display & limit FPS
    pygame.display.flip()
    clock.tick(60)

pygame.quit()