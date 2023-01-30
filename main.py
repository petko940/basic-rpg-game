import pygame

from menu_class import Menu

pygame.init()

WIDTH, HEIGHT = (1920, 1080)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

menu = Menu()
game_running = True

while game_running:
    menu.podmenu1()
    menu.menu()

    pygame.display.flip()

pygame.quit()
