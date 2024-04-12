# player.py

import pygame

class Player:
    def __init__(self, pos_x, pos_y, color):
        self.color = color
        self.width = 20
        self.height = 20
        self.x = pos_x
        self.y = pos_y
        self.velocity_x = 0
        self.velocity_y = 0
        self.top_speed = 5
        self.acceleration = 0.2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.on_platform = False
        self.checkpoint_reached = False
        self.distance_traveled = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.on_platform:
            self.velocity_y = -10
        if keys[pygame.K_RIGHT]:
            if self.velocity_x < self.top_speed:
                self.velocity_x += self.acceleration
        elif keys[pygame.K_LEFT]:
            if self.velocity_x > -self.top_speed:
                self.velocity_x -= self.acceleration
        else:
            self.velocity_x *= 0.9
        if self.x <= 0:
            self.x = 0
        elif self.x >= 1200 - self.width:
            self.x = 1200 - self.width

    def apply_gravity(self):
        self.velocity_y += 0.5
        self.y += self.velocity_y
        if self.y >= 300 - self.height:
            self.y = 300 - self.height
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
