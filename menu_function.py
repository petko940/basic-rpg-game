import pygame

menu_image = pygame.image.load('images/menu/menu.jpg')
button_play = pygame.image.load('images/menu/play.png')
button_play_rect = button_play.get_rect()
button_play_rect.move_ip(850, 400)


def menu_func(running_menu, screen):
    while running_menu:
        screen.blit(menu_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_play_rect.collidepoint(event.pos):
                    pass

        pygame.draw.rect(screen, (255, 0, 0), button_play_rect, 10)
        screen.blit(button_play, (800, 400))
        pygame.display.flip()
        # print(button_quit.get_rect())
