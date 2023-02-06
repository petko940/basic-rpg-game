import pygame

from menu_class import Menu

pygame.init()

WIDTH, HEIGHT = (1920, 1080)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

menu = Menu()
game_running = True

a = pygame.Rect(0, 0, 1920, 1080)
while game_running:
    menu.menu()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False

    pygame.draw.rect(screen, (255, 0, 0), a)
    pygame.display.flip()

pygame.quit()
