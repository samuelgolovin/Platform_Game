# game_over.py

import pygame

class GameOver:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.Surface((width, height))
        self.font = pygame.font.Font(None, 48)

    def draw(self, surface):
        self.screen.fill((0, 0, 0))
        text_surface = self.font.render("Game Over", True, (255, 0, 0))
        text_surface1 = self.font.render("Press Enter to Go to START", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
        text_rect1 = text_surface1.get_rect(center=(self.width // 2, self.height // 2 + self.height // 4))
        self.screen.blit(text_surface, text_rect)
        self.screen.blit(text_surface1, text_rect1)
        surface.blit(self.screen, (0, 0))
