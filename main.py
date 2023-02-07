import pygame

from menu_class import Menu
from warrior_character import Warrior

pygame.init()

WIDTH, HEIGHT = (1920, 1080)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

menu = Menu()
game_running = True

a = pygame.Rect(0, 0, 1920, 1080)

warrior = Warrior()
while game_running:
    # menu.menu()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            # elif event.key == pygame.K_d:
            #     screen.blit(warrior.walk_images("right"),warrior.idle_animation("right").get_rect())
                # TO DO walk right
                # char.walking = True
    if pygame.key.get_pressed()[pygame.K_d]:
        screen.blit(warrior.walk_images("right"), warrior.idle_animation("right").get_rect())
        pygame.display.flip()

    screen.blit(warrior.idle_animation("right"),(100,100))

    pygame.display.flip()

pygame.quit()
