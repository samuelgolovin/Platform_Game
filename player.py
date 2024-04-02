# player.py

import pygame

class Player:
    def __init__(self, width, height):
        self.color = (255, 255, 255)
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.on_platform = False
        self.checkpoint_reached = False
        self.distance_traveled = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.on_platform:
            self.velocity_y = -10
        if keys[pygame.K_RIGHT]:
            if self.velocity_x < 5:
                self.velocity_x += 0.2
        elif keys[pygame.K_LEFT]:
            if self.velocity_x > -5:
                self.velocity_x -= 0.2
        else:
            self.velocity_x *= 0.9

    def apply_gravity(self):
        self.velocity_y += 0.5
        self.y += self.velocity_y
        if self.y >= 400 - self.height:
            self.y = 400 - self.height
            self.velocity_y = 0
            self.on_platform = True
        else:
            self.on_platform = False

    def apply_velocity_x(self):
        self.x += self.velocity_x

    def draw(self, surface, camera_offset):
        pygame.draw.rect(surface, self.color, (self.x - camera_offset, self.y, self.width, self.height))

    def update(self):
        self.player_input()
        self.apply_velocity_x()
        self.apply_gravity()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.distance_traveled += abs(self.velocity_x)
