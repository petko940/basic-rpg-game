import pygame

menu_image = pygame.image.load('images/menu/menu.jpg')
button_play = pygame.image.load('images/menu/play.png')
button_play_rect = button_play.get_rect()
print(button_play_rect)

def menu_func(running_menu, screen):
    while running_menu:
        screen.blit(menu_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_ = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.collidepoint(event.pos):
                #     menu_ = False
                pass
        screen.blit(button_play,(200,200))
        pygame.display.flip()
        # print(button_quit.get_rect())
