import pygame

from menu_class import Menu
from warrior_character import Warrior
from class_maps.map_controller import MapController
from actions import Actions

pygame.init()

WIDTH, HEIGHT = (1920, 1080)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

map_controller = MapController()
map_controller.create_map([pygame.image.load(f'images/maps/map1/({i}).png') for i in range(1, 5 + 1)], "Forest")

menu = Menu()
game_running = True

a = pygame.Rect(0, 0, 1920, 1080)

warrior = Warrior()
actions = Actions()
while game_running:
    # menu.menu()
    screen.blit(map_controller.show_current_map(), (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            # elif event.key == pygame.K_d:
            #     screen.blit(warrior.walk_images("right"),warrior.idle_animation("right").get_rect())
            # TO DO walk right
            # char.walking = True

    if pygame.key.get_pressed()[pygame.K_d]:
        screen.blit(warrior.walk_images("right"), actions.walk())

        pygame.display.update()
    else:
        screen.blit(warrior.idle_animation('right'), actions.walk())

        pygame.display.flip()

pygame.quit()
