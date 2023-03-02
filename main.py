import pygame

from characters.hero_controller import HeroController
from menu_class import Menu
from class_maps.map_controller import MapController
from default_properties import load_data, save_on_close

# timer 83 , 151
from timer import timer
import time

pygame.init()


def loading_game_screen(window, current_map: MapController, hero: object, rect_of_background: pygame.Rect):
    for i in range(510, 0, -1):
        window.blit(current_map.show_current_map(), (0, 0))
        window.blit(hero.idle_animation("right"), hero.idle())  # NOQA
        pygame.draw.rect(window, (50, (255 - i // 2), 0), rect_of_background, int(i * 1.1))
        pygame.display.update()


WIDTH, HEIGHT = (1366, 768)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
resized = 1.4

action_bar_image = pygame.image.load('images/action_bar.png')
action_bar_x_pos, action_bar_y_pos = (WIDTH // 2) - (action_bar_image.get_rect().width // 2), 675

map_controller = MapController()
map_controller.create_map(
    [pygame.transform.scale(pygame.image.load(f'images/maps/map1/({i}).png'), (1920 / resized, 1080 / resized)) for i in
     range(1, 5 + 1)], "Forest")

hero_controller = HeroController()
hero_controller.create_hero("Warrior", 20, 200)
hero_controller.create_hero("Mage", 20, 200)
hero_controller.create_hero("Hunter", 20, 200)

warrior = hero_controller.get_hero_object("Warrior")
mage = hero_controller.get_hero_object("Mage")
hunter = hero_controller.get_hero_object("Hunter")

collected_game_info = load_data()

map_controller.current_map = collected_game_info["Map"]['current_map']
warrior.level = collected_game_info["Warrior"]['level']
mage.level = collected_game_info["Mage"]['level']
hunter.level = collected_game_info["Hunter"]['level']

menu = Menu(warrior, mage, hunter)

# menu.display_beginning_image() skipping the beginning image
menu.menu()
current_hero = menu.chosen_hero

background_rect = map_controller.show_current_map().get_rect()

# loading_game_screen(screen, map_controller, current_hero, background_rect)  # for faster loading screen


################################################################
"""
testing to see if the methods Tamer wrote are working
you can keep this class for now to test health bars in the future
"""


class Monster:

    def __init__(self):
        self.damage = 5


monster = Monster()

# print(current_hero.health_bar)
# hero_controller.take_damage(current_hero, monster)
# print(current_hero.health_bar)
# print(hero_controller.check_if_hero_died(current_hero))
################################################################

start_time = time.time()

game_running = True
while game_running:
    pygame.time.Clock().tick(100)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False

            # means that a skill is currently animating
            if hero_controller.skill_to_use or current_hero.is_attacking:
                continue

            elif event.key == pygame.K_5:
                hero_controller.take_damage(current_hero, monster)

            elif event.key == pygame.K_1:
                current_hero.is_attacking = True
                hero_controller.skill_to_use = 1

            # healing spell
            elif event.key == pygame.K_2:
                hero_controller.skill_to_use = 2

            elif event.key == pygame.K_3:
                current_hero.is_attacking = True
                hero_controller.skill_to_use = 3

            elif event.key == pygame.K_4:
                current_hero.is_attacking = True
                hero_controller.skill_to_use = 4

    screen.blit(map_controller.show_current_map(), (0, 0))

    hero_controller.display_health_and_mana_bars(screen, current_hero)
    hero_controller.display_health_and_mana_stats(screen, current_hero)
    hero_controller.display_hero_frame_and_level(screen, current_hero)

    screen.blit(action_bar_image, (action_bar_x_pos, action_bar_y_pos))

    # must fix isinstance, when we add all the skill icons
    hero_controller.display_skill_icons(screen, current_hero, action_bar_x_pos, action_bar_y_pos)

    # shows skill description if you hover on a skill icon
    hero_controller.show_skill_description(screen, current_hero, pygame.mouse.get_pos())

    # calling the skills animations on button press
    hero_controller.use_skill(current_hero, screen)

    if current_hero.is_attacking:
        screen.blit(current_hero.attack_animation(), current_hero.get_hero_pos())

    elif pygame.key.get_pressed()[pygame.K_d]:
        if not current_hero.is_right_direction:
            current_hero.change_direction()

        current_hero.walk()
        screen.blit(current_hero.walk_images(), current_hero.get_hero_pos())

        map_controller.check_for_traverse(current_hero)

    elif pygame.key.get_pressed()[pygame.K_a]:
        if current_hero.is_right_direction:
            current_hero.change_direction()

        current_hero.walk()
        screen.blit(current_hero.walk_images(), current_hero.get_hero_pos())

        map_controller.check_for_traverse(current_hero)

    else:
        if not current_hero.is_attacking:
            screen.blit(current_hero.idle_animation(), current_hero.get_hero_pos())

    timer(start_time, screen)
    pygame.display.update()

pygame.quit()

progress_of_game = {
    "Map": {'current_map': map_controller.current_map},
    "Hunter": {'level': hunter.level, 'health': hunter.health, 'mana': hunter.mana},
    "Mage": {'level': mage.level, 'health': mage.health, 'mana': mage.mana},
    "Warrior": {'level': warrior.level, 'health': warrior.health},
}
save_on_close(progress_of_game)
