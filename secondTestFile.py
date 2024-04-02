import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAVITY = 0.5
JUMP_VELOCITY = -10
MAX_VELOCITY_X = 5
CAMERA_THRESHOLD = 200  # Adjust this value to set the distance before camera offset starts

# Player class
class Player:
    def __init__(self):
        # Initialize player attributes
        self.color = WHITE
        self.width = 20
        self.height = 20
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.velocity_x = 0
        self.velocity_y = 0
        # Create a rectangle to represent the player's position and size
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.on_platform = False
        self.checkpoint_reached = False
        self.distance_traveled = 0

    def player_input(self):
        # Handle player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.on_platform:
            self.velocity_y = JUMP_VELOCITY
        if keys[pygame.K_RIGHT]:
            if self.velocity_x < MAX_VELOCITY_X:
                self.velocity_x += 0.2
        elif keys[pygame.K_LEFT]:
            if self.velocity_x > -MAX_VELOCITY_X:
                self.velocity_x -= 0.2
        else:
            self.velocity_x *= 0.9  # Apply friction

    def apply_gravity(self):
        # Apply gravity to the player
        self.velocity_y += GRAVITY
        self.y += self.velocity_y

        # Check if player is on a platform
        if self.y >= HEIGHT - self.height:
            self.y = HEIGHT - self.height
            self.velocity_y = 0
            self.on_platform = True
        else:
            self.on_platform = False

    def apply_velocity_x(self):
        # Apply horizontal velocity to the player
        self.x += self.velocity_x

    def draw(self, surface, camera_offset):
        # Draw the player on the screen, adjusting for camera offset in the x-direction only
        pygame.draw.rect(surface, self.color, (self.x - camera_offset, self.y, self.width, self.height))

    def update(self, surface):
        # Update player's state
        self.player_input()
        self.apply_velocity_x()
        self.apply_gravity()
        # Update the player's rectangle position
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # Update distance traveled
        self.distance_traveled += abs(self.velocity_x)

class Platform:
    def __init__(self, x, y, width, height):
        # Initialize platform attributes
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, camera_offset):
        # Draw the platform on the screen without adjusting for camera offset in the y-direction
        pygame.draw.rect(surface, WHITE, (self.rect.x - camera_offset, self.rect.y, self.rect.width, self.rect.height))

# Initialize pygame
pygame.init()
# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Create a clock object to control the frame rate
clock = pygame.time.Clock()
# Create the player object
player = Player()
# Create a list of platform objects
platforms = [
    Platform(200, 200, 100, 10),
    Platform(300, 300, 100, 10),
    Platform(450, 250, 100, 10),
    Platform(600, 200, 100, 10),
    Platform(700, 150, 100, 10),
    Platform(800, 100, 100, 10),  # Checkpoint platform
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player's state and check collisions with platforms
    player.update(screen)
    for platform in platforms:
        if player.rect.colliderect(platform.rect):
            if player.velocity_y > 0:  # Check if player is moving downwards
                player.y = platform.rect.top - player.height
                player.velocity_y = 0
                player.on_platform = True
            if platform == platforms[-1]:  # Checkpoint reached
                player.checkpoint_reached = True

    # Calculate camera offset to follow the player in the x-direction only after reaching threshold distance
    camera_offset = max(0, player.x - WIDTH // 2) if player.distance_traveled > CAMERA_THRESHOLD else 0

    # Clear the screen
    screen.fill(BLACK)
    # Draw platforms
    for platform in platforms:
        platform.draw(screen, camera_offset)
    # Draw the player
    player.draw(screen, camera_offset)

    if player.checkpoint_reached:
        # Display checkpoint reached message
        font = pygame.font.SysFont(None, 36)
        text = font.render("You reached the checkpoint! Game finished!", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
# Exit the program
sys.exit()
