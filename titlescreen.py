# titlescreen.py

import pygame

class TitleScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.draw_text("Super Awesome Platform Game", (255, 255, 255), surface, 250, 150)
        self.draw_text("Press Enter to Start", (255, 255, 255), surface, 300, 250)

    def draw_text(self, text, color, surface, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
