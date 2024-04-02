# titlescreen.py

import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

class TitleScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Title Screen Example")

    def draw_text(self, text, font, color, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobj, textrect)

    def show(self):
        font = pygame.font.Font(None, 36)
        running = True

        while running:
            self.screen.fill(BLACK)
            self.draw_text("Super Awesome Platform Game", font, WHITE, WIDTH//2 - 200, HEIGHT//2 - 100)

            # Start button
            start_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2, 200, 50)
            pygame.draw.rect(self.screen, GRAY, start_button)
            self.draw_text("Start Game", font, BLACK, start_button.x + 20, start_button.y + 10)

            # Exit button
            exit_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 100, 200, 50)
            pygame.draw.rect(self.screen, GRAY, exit_button)
            self.draw_text("Exit Game", font, BLACK, exit_button.x + 20, exit_button.y + 10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if start_button.collidepoint(mouse_pos):
                        break
                        running = False  # Exit the title screen and start the game
                    elif exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

            pygame.time.Clock().tick(30)

            return False
