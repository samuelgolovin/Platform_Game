# menu.py

import pygame

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.Surface((width, height))
        self.font = pygame.font.Font(None, 36)
        self.menu_items = ["Resume (P)", "Main Menu (M)", "Quit (Q)"]
        self.selected_item = 0

    def draw(self, surface):
        self.screen.fill((0, 0, 0))
        for index, item in enumerate(self.menu_items):
            color = (255, 255, 255) if index == self.selected_item else (128, 128, 128)
            text_surface = self.font.render(item, True, color)
            text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2 + index * 40))
            self.screen.blit(text_surface, text_rect)
        surface.blit(self.screen, (0, 0))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_item = (self.selected_item - 1) % len(self.menu_items)
            elif event.key == pygame.K_DOWN:
                self.selected_item = (self.selected_item + 1) % len(self.menu_items)
            elif event.key == pygame.K_RETURN:
                if self.selected_item == 0:
                    return "Resume"
                elif self.selected_item == 1:
                    return "Main Menu"
                elif self.selected_item == 2:
                    return "Quit"
        return None
