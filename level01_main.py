import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 400
BLACK = (0, 0, 0)
LIGHT_BLUE = (137, 207, 240)
LIGHT_GREEN = (190, 204, 154)
PINK = (246, 180, 199)
CAMERA_THRESHOLD = HEIGHT / 2
GAME_VARS = {
    "player_x": 200,
    "player_y": 200,
    "enemy_x": 500,
    "enemy_y": 200
}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, LIGHT_GREEN, (0, 300, WIDTH, HEIGHT))
    pygame.draw.rect(screen, PINK, (50, 280, 20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()