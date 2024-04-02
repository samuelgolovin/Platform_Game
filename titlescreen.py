
GRAY = (200, 200, 200)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def title_screen():
    font = pygame.font.Font(None, 36)
    running = True

    while running:
        screen.fill(BLACK)
        draw_text("Super Awesome Platform Game", font, WHITE, screen, WIDTH/2 - 100, HEIGHT/2 - 100)

         # Start button
        start_button = pygame.Rect(WIDTH/2 - 100, HEIGHT/2, 200, 50)
        pygame.draw.rect(screen, GRAY, start_button)
        draw_text("Start Game", font, BLACK, screen, start_button.x + 20, start_button.y + 10)

        # Exit button
        exit_button = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 + 100, 200, 50)
        pygame.draw.rect(screen, GRAY, exit_button)
        draw_text("Exit Game", font, BLACK, screen, exit_button.x + 20, exit_button.y + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if start_button.collidepoint(mouse_pos):
                    running = False  # Exit the title screen and start the game
                elif exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

        pygame.time.Clock().tick(30)
