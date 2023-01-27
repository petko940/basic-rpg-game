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
    pygame.display.flip()

pygame.quit()
