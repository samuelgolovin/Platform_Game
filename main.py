# main.py

import pygame
import sys
from player import Player
from platform import Platform
from enemy import Enemy
from menu import Menu
from game_over import GameOver  # Import the GameOver class
from titlescreen import TitleScreen

# Constants
WIDTH, HEIGHT = 800, 400
BLACK = (0, 0, 0)
CAMERA_THRESHOLD = 200

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create player, platforms, and enemy
player = Player(20, 20)
platforms = [
    Platform(200, 200, 100, 10),
    Platform(300, 300, 100, 10),
    Platform(450, 250, 100, 10),
    Platform(600, 200, 100, 10),
    Platform(700, 150, 100, 10),
    Platform(800, 100, 100, 10),  # Checkpoint platform
]
enemy = Enemy(600, 100, 20, 20)

# Create a menu instance
title_screen = TitleScreen()
menu = Menu(WIDTH, HEIGHT)

# Create a game over instance
game_over_screen = GameOver(WIDTH, HEIGHT)

# Variables for game state and menu visibility
running = True
game_started = True
game_paused = False
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_paused = not game_paused
            elif event.key == pygame.K_m:
                game_paused = True
            elif event.key == pygame.K_q:
                running = False

    if not (game_paused or game_over):
        player.update()
        for platform in platforms:
            if player.rect.colliderect(platform.rect):
                if player.velocity_y > 0:
                    player.y = platform.rect.top - player.height
                    player.velocity_y = 0
                    player.on_platform = True
                if platform == platforms[-1]:
                    player.checkpoint_reached = True

        enemy.update()

        if enemy.check_collision(player.rect):
            game_over = True

        camera_offset = max(0, player.x - WIDTH // 2) if player.distance_traveled > CAMERA_THRESHOLD else 0

        screen.fill(BLACK)
        for platform in platforms:
            platform.draw(screen, camera_offset)
        player.draw(screen, camera_offset)
        enemy.draw(screen, camera_offset)

        if player.checkpoint_reached:
            font = pygame.font.SysFont(None, 36)
            text = font.render("You reached the checkpoint! Game finished!", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        elif game_over:
            game_over_screen.draw(screen)
    else:
        menu.draw(screen)
        menu_action = menu.handle_event(event)
        if menu_action == "Resume":
            game_paused = False
        elif menu_action == "Main Menu":
            # Implement logic to go back to the main menu
            pass
        elif menu_action == "Quit":
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
