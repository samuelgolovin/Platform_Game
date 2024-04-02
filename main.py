# main.py

import pygame
import sys
from player import Player
from platform import Platform
from enemy import Enemy
from menu import Menu  # Import the Menu class

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
enemy = Enemy(600, 100, 20, 20)  # Create an instance of the updated Enemy class

# Create a menu instance
menu = Menu(WIDTH, HEIGHT)

# Variables for game state and menu visibility
running = True
game_paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pause the game if "P" is pressed
                game_paused = not game_paused
            elif event.key == pygame.K_m:  # Show menu if "M" is pressed
                game_paused = True

    if not game_paused:
        # Update player's state and check collisions with platforms
        player.update()
        for platform in platforms:
            if player.rect.colliderect(platform.rect):
                if player.velocity_y > 0:
                    player.y = platform.rect.top - player.height
                    player.velocity_y = 0
                    player.on_platform = True
                if platform == platforms[-1]:
                    player.checkpoint_reached = True

        # Update enemy's state
        enemy.update()

        # Check collision with enemy
        if enemy.check_collision(player.rect):
            running = False  # End the game if the player touches the enemy

        # Calculate camera offset to follow the player in the x-direction only after reaching threshold distance
        camera_offset = max(0, player.x - WIDTH // 2) if player.distance_traveled > CAMERA_THRESHOLD else 0

        # Clear the screen
        screen.fill(BLACK)
        # Draw platforms
        for platform in platforms:
            platform.draw(screen, camera_offset)
        # Draw the player
        player.draw(screen, camera_offset)
        # Draw the enemy
        enemy.draw(screen, camera_offset)

        if player.checkpoint_reached:
            font = pygame.font.SysFont(None, 36)
            text = font.render("You reached the checkpoint! Game finished!", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        elif not running:
            font = pygame.font.SysFont(None, 36)
            text = font.render("Game over! You touched the enemy.", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    else:
        # Draw menu if the game is paused
        menu.draw(screen)
        # Handle menu events
        menu_action = menu.handle_event(event)
        if menu_action == "Resume":
            game_paused = False
        elif menu_action == "Main Menu":
            # Implement logic to go back to the main menu
            pass
        elif menu_action == "Quit":
            running = False

    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
# Exit the program
sys.exit()
