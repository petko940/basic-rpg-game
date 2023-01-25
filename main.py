from menu_function import menu_func
import pygame

pygame.init()

WIDTH, HEIGHT = (1920, 1080)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


menu_ = True

game_running = True
while game_running:
    if menu_:
        menu_ = menu_func(menu_, screen)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu_ = True
    #     elif event.type == pygame.MOUSEBUTTONDOWN:
    #         # Check if the mouse cursor is within the button's rectangle
    #         if button_rect_quit.collidepoint(event.pos):
    #             quit()
    # screen.blit(button_quit, button_rect_quit)
    # screen.blit(title_quit, (button_rect_quit.x + 50, button_rect_quit.y + 17))
    #
    # screen.blit(button_quit, button_rect_play)
    # screen.blit(title_play, (button_rect_play.x + 50, button_rect_play.y + 17))
    pygame.display.flip()

pygame.quit()
