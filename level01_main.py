import pygame
import sys
from level01_player import Player
from level01_enemy import Enemy
from level01_platform import Platform

pygame.init()

WIDTH, HEIGHT = 800, 400
BLACK = (0, 0, 0)
LIGHT_BLUE = (137, 207, 240)
LIGHT_GREEN = (190, 204, 154)
PINK = (246, 180, 199)
CAMERA_THRESHOLD = 200
GAME_VARS = {
    "player_x": 200,
    "player_y": 200,
    "enemy_x": 500,
    "enemy_y": 200,
    "enemy_x_size": 30,
    "enemy_y_size": 30,
}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def create_player():
    return Player(GAME_VARS["player_x"], GAME_VARS["player_y"], PINK)
def create_enemy():
    return Enemy(GAME_VARS["enemy_x"], GAME_VARS["enemy_y"], GAME_VARS["enemy_x_size"], GAME_VARS["enemy_y_size"])

player = create_player()
enemy = create_enemy()

platforms = [
    Platform(150, 200, 100, 10),
    Platform(300, 300, 100, 10),
    Platform(450, 250, 100, 10),
    Platform(600, 200, 100, 10),
    Platform(750, 150, 100, 10),
    Platform(900, 100, 100, 10),  # Checkpoint platform
]

running = True
game_started = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game_started:
        if player.x < 800:
            camera_offset = max(0, player.x - WIDTH // 2) if player.distance_traveled > CAMERA_THRESHOLD else 0
        else: camera_offset = 400
        #update things
        player.update()
        enemy.update()
        for platform in platforms:
                if player.rect.colliderect(platform.rect):
                    if player.velocity_y > 0:
                        player.y = platform.rect.top - player.height
                        player.velocity_y = 0
                        player.on_platform = True
                    if platform == platforms[-1]:
                        player.checkpoint_reached = True
        for platform in platforms:
                if enemy.rect.colliderect(platform.rect):
                    if enemy.velocity_y > 0:
                        enemy.y = platform.rect.top - enemy.height
                        enemy.velocity_y = 0
                        enemy.on_platform = True
                    if platform == platforms[-1]:
                        enemy.checkpoint_reached = True
        #draw the things
        screen.fill(LIGHT_BLUE)
        for platform in platforms:
            platform.draw(screen, camera_offset)
        pygame.draw.rect(screen, LIGHT_GREEN, (0, 300, WIDTH, HEIGHT))
        enemy.draw(screen, camera_offset)
        player.draw(screen, camera_offset)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()