import pygame
import random
class Enemy:
    def __init__(self, pos_x, pos_y, color, width, height):
        self.color = color
        self.width = width
        self.height = height
        self.x = pos_x
        self.y = pos_y
        self.top_speed = 2.5
        self.acceleration = 0.2
        self.velocity_x = 0
        self.velocity_y = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.on_platform = False

        self.jump_timer = 0
        self.jump_interval = random.randint(120, 240)

    def draw(self, surface, camera_offset):
        pygame.draw.rect(surface, self.color, (self.x - camera_offset, self.y, self.width, self.height))

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect)
    
    def follow_player(self, player_x):
        if self.x < player_x:
            if self.velocity_x < self.top_speed:
                self.velocity_x += self.acceleration
        else:
            if self.velocity_x > -self.top_speed:
                self.velocity_x -= self.acceleration

    def apply_velocity_x(self):
        self.x += self.velocity_x
    
    def apply_gravity(self):
        self.velocity_y += 0.5
        self.y += self.velocity_y
        if self.y >= 300 - self.height:
            self.y = 300 - self.height
            self.velocity_y = 0
            self.on_platform = True
        else:
            self.on_platform = False
    
    def jump(self):
        self.velocity_y = -10
    
    def jump_handle(self):
        self.jump_timer += 1
        if self.jump_timer >= self.jump_interval and self.on_platform:
            self.jump()
            self.jump_timer = 0
            self.jump_interval = random.randint(120, 240)

    def update(self, player_x):
        self.follow_player(player_x)
        self.jump_handle()
        self.apply_gravity()
        self.apply_velocity_x()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)