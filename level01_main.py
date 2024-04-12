import pygame
import sys
import random
from level01_player import Player
from level01_enemy import Enemy
from level01_platform import Platform
from level01_titlescreen import TitleScreen
from level01_game_over import GameOver
from level01_particles import Particle

pygame.init()

WIDTH, HEIGHT = 800, 400

BLACK = (0, 0, 0)
LIGHT_BLUE = (137, 207, 240)
LIGHT_GREEN = (190, 204, 154)
PINK = (246, 180, 199)
YELLOW = (255, 175, 69)
ORANGE = (251, 109, 72)
DARK_PINK = (215, 75, 118)
PURPLE = (103, 63, 105)

CAMERA_THRESHOLD = 200
GAME_VARS = {
    "player_x": 200,
    "player_y": 200,
    "enemy_x": 500,
    "enemy_y": 200,
    "enemy_x_size": 20,
    "enemy_y_size": 20,
}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

titlescreen = TitleScreen()
gameoverscreen = GameOver(WIDTH, HEIGHT)

def create_player():
    return Player(GAME_VARS["player_x"], GAME_VARS["player_y"], YELLOW)
def create_enemy():
    return Enemy(GAME_VARS["enemy_x"], GAME_VARS["enemy_y"], DARK_PINK, GAME_VARS["enemy_x_size"], GAME_VARS["enemy_y_size"])

player = create_player()
enemy = create_enemy()

# Create a list to store particles
particles = []
# Create particles and add them to the list
for _ in range(20):
    position = [player.x + player.width / 2, player.y + player.height / 2]
    velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
    color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255), 255)
    size = random.uniform(5, 8)
    lifespan = random.randint(20, 30)
    particle = Particle(position, velocity, color, size, lifespan)
    particles.append(particle)

platforms = [
    Platform(150, 200, 100, 10),
    Platform(300, 300, 100, 10),
    Platform(450, 250, 100, 10),
    Platform(600, 200, 100, 10),
    Platform(750, 150, 100, 10),
    Platform(900, 100, 100, 10),  # Checkpoint platform
]

running = True
game_started = False
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game_over:
        gameoverscreen.draw(screen)
        # take game to titlescreen
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            player = create_player()
            enemy = create_enemy()
            game_over = False
            titlescreen.draw(screen)
            # Start the game when Enter is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_started = True

    elif game_started:
        if player.x < 800:
            camera_offset = max(0, player.x - WIDTH // 2) if player.distance_traveled > CAMERA_THRESHOLD else 0
        else: camera_offset = 400
        #update things
        player.update()
        enemy.update(player.x)
        # Update particles
        for particle in particles:
            particle.update(player.x + player.width / 2, player.y + player.height / 2)

        if enemy.check_collision(player.rect):
                game_over = True
                game_started = False
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
        screen.fill(ORANGE)
        for platform in platforms:
            platform.draw(screen, camera_offset)
        pygame.draw.rect(screen, PURPLE, (0, 300, WIDTH, HEIGHT))
        # Draw particles
        for particle in particles:
            particle.draw(screen, camera_offset)
        enemy.draw(screen, camera_offset)
        player.draw(screen, camera_offset)

    # titlescreen
    else:
        titlescreen.draw(screen)
        # Start the game when Enter is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            game_started = True
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()