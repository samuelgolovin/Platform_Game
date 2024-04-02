# enemy.py

import pygame

class Enemy:
    def __init__(self, x, y, width, height):
        self.color = (255, 0, 0)  # Red color for enemy
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.velocity_x = 2  # Initial velocity in the x-direction
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface, camera_offset):
        pygame.draw.rect(surface, self.color, (self.x - camera_offset, self.y, self.width, self.height))

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect)

    def update(self):
        self.x += self.velocity_x
        self.rect.x = self.x

        # Reverse direction if enemy reaches screen boundaries
        if self.x <= 0 or self.x >= 800 - self.width:
            self.velocity_x *= -1
