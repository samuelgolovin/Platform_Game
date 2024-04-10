import pygame

class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, camera_offset):
        pygame.draw.rect(surface, (255, 255, 255), (self.rect.x - camera_offset, self.rect.y, self.rect.width, self.rect.height))
