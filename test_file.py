import pygame
import random

class Particle:
    def __init__(self, position, velocity, color, size, lifespan):
        self.position = position
        self.velocity = velocity
        self.color = color
        self.size = size
        self.lifespan = lifespan
        self.age = 0  # Initial age of the particle

    def update(self):
        # Update particle position based on velocity
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        # Increase particle age
        self.age += 1

        # Reset particle if it reaches the end of its lifespan
        if self.age >= self.lifespan:
            self.position = [random.randint(0, 800), random.randint(0, 400)]
            self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
            self.size = random.uniform(5, 10)
            self.lifespan = random.randint(30, 60)
            self.age = 0

        # Shrink particle size over time
        self.size -= 0.1

        # Fade out particle color over time
        alpha = int(255 * (1 - self.age / self.lifespan))
        self.color = (self.color[0], self.color[1], self.color[2], alpha)

    def draw(self, surface):
        # Draw the particle on the surface
        pygame.draw.circle(surface, self.color, (int(self.position[0]), int(self.position[1])), int(self.size))

# Create a list to store particles
particles = []

# Create particles and add them to the list
for _ in range(100):
    position = [random.randint(0, 800), random.randint(0, 400)]
    velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
    size = random.uniform(5, 10)
    lifespan = random.randint(30, 60)
    particle = Particle(position, velocity, color, size, lifespan)
    particles.append(particle)

# Main loop
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update particles
    for particle in particles:
        particle.update()

    # Draw particles
    screen.fill((0, 0, 0))
    for particle in particles:
        particle.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
