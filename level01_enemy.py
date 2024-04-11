import pygame
import random
class Enemy:
    def __init__(self, pos_x, pos_y, width, height):
        self.color = (255, 0, 0)  # Red color for enemy
        self.width = 20
        self.height = 20
        self.x = pos_x
        self.y = pos_y
        self.velocity_x = -1
        self.velocity_y = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.on_platform = False

        self.jump_timer = 0
        self.jump_interval = random.randint(120, 240)

    def draw(self, surface, camera_offset):
        pygame.draw.rect(surface, self.color, (self.x - camera_offset, self.y, self.width, self.height))

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect)
    
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

    def enemy_AI(self):
        if self.x < 0:
            self.velocity_x *= -1
            self.x = 0
        elif self.x > 1200 - self.width:
            self.velocity_x *= -1
            self.x = 1200 - self.width
    
    def jump(self):
        if self.y >= 300 - self.height: self.velocity_y = -10
    
    def jump_handle(self):
        self.jump_timer += 1
        if self.jump_timer >= self.jump_interval:
            self.jump()
            self.jump_timer = 0
            self.jump_interval = random.randint(120, 240)

    def update(self):
        self.jump_handle()
        self.enemy_AI()
        self.apply_gravity()
        self.apply_velocity_x()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)