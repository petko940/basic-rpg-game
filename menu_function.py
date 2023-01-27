import pygame

buttons_x, buttons_y = 1920 / 2 - 200, 1080 / 2 - 150
menu_image = pygame.image.load('images/menu/menu.jpg')

button_play = pygame.image.load('images/menu/play.png')
button_play_rect = button_play.get_rect()
button_play_rect.x = buttons_x
button_play_rect.y = buttons_y

button_quit = pygame.image.load('images/menu/exit.png')
button_quit_rect = button_quit.get_rect()
button_quit_rect.x = buttons_x
button_quit_rect.y = buttons_y + 100

print(button_play_rect)


def menu_func(running_menu, screen):
    global mouse_pos
    while running_menu:
        screen.blit(menu_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_quit_rect.collidepoint(mouse_pos):
                    quit()

        screen.blit(button_play, button_play_rect)
        screen.blit(button_quit, button_quit_rect)
        pygame.display.flip()

        # print(button_quit.get_rect())
