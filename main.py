import pygame

pygame.init()
menu = pygame.image.load('images/menu/menu.jpg')

SIZE = (1920, 1080)
screen = pygame.display.set_mode(SIZE)

font = pygame.font.Font(None, 30)
title_quit = font.render("QUIT", True, (255, 255, 255))
title_play = font.render("PLAY", True, (255, 255, 255))

button_quit = pygame.Surface((150, 50))
button_quit.fill((255, 0, 0))

button_rect_quit = pygame.Rect(1920 // 2, 1080 // 2 - 100, 100, 100)
button_rect_play = pygame.Rect(1920 // 2, 1080 // 2 - 200, 100, 100)

running = True
while running:
    screen.blit(menu, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse cursor is within the button's rectangle
            if button_rect_quit.collidepoint(event.pos):
                quit()
    screen.blit(button_quit, button_rect_quit)
    screen.blit(title_quit, (button_rect_quit.x + 50, button_rect_quit.y + 17))

    screen.blit(button_quit, button_rect_play)
    screen.blit(title_play, (button_rect_play.x + 50, button_rect_play.y + 17))
    pygame.display.flip()

pygame.quit()
