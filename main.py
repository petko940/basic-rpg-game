import pygame

from characters.hero_controller import HeroController
from menu_class import Menu
from class_maps.map_controller import MapController
from monsters.demon import Demon
from monsters.jinn import Jinn
from monsters.lizard import Lizard
from monsters.medusa import Medusa
from monsters.mini_dragon import MiniDragon
from monsters.monster_controller import MonsterController
from data_processor import DataProcessor
from utils import get_screen_size

pygame.init()


def loading_game_screen(window, current_map: MapController, hero, rect_of_background: pygame.Rect):
    for i in range(510, 0, -1):
        window.blit(current_map.show_current_map(), (0, 0))
        window.blit(hero.idle_animation(), hero.get_hero_pos())
        pygame.draw.rect(window, (50, (255 - i // 2), 0), rect_of_background, int(i * 1.1))
        pygame.display.update()


def load_maps(map_controller_obj):
    maps = (
        ([pygame.transform.scale(pygame.image.load(f'images/maps/map1/({i}).png').convert_alpha(), (1366, 768)) for i in range(1, 5 + 1)], "Forest"),
        ([pygame.image.load(f'images/maps/map2/{i}.png').convert_alpha() for i in range(5)], "NarrowForest"),
        ([pygame.image.load(f'images/maps/map3/{i}.png').convert_alpha() for i in range(5)], "BigTreeForest"),
        ([pygame.image.load(f'images/maps/map4/{i}.png').convert_alpha() for i in range(5)], "Bridge"),
        ([pygame.image.load(f'images/maps/map5/{i}.png').convert_alpha() for i in range(5)], "GreenBigForest"),
        )

    for images, map_name in maps:
        map_controller_obj.create_map(images, map_name)


WIDTH, HEIGHT = get_screen_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
resized = 1.4

action_bar_image = pygame.image.load('images/action_bar.png')
action_bar_x_pos, action_bar_y_pos = (WIDTH // 2) - (action_bar_image.get_rect().width // 2), 675


hero_controller = HeroController()
hero_controller.create_hero("Warrior", 20, 200)
hero_controller.create_hero("Mage", 20, 200)
hero_controller.create_hero("Hunter", 20, 200)
hero_controller.gather_caster_skills()

warrior = hero_controller.get_hero_object("Warrior")
mage = hero_controller.get_hero_object("Mage")
hunter = hero_controller.get_hero_object("Hunter")


menu = Menu(warrior, mage, hunter)


map_controller = MapController(menu.arrow)
load_maps(map_controller)


demon = Demon(100, 15, 1400, 210)  # [health, damage, x_pos, y_pos]
jinn = Jinn(100, 15, 1400, 210)
mini_dragon = MiniDragon(100, 15, 1400, 310)
lizard = Lizard(100, 15, 1400, 250)
medusa = Medusa(100, 15, 1400, 250)
monster_controller = MonsterController(medusa, lizard, mini_dragon, jinn, demon)


set_hero_data = DataProcessor([warrior, mage, hunter])
set_hero_data.set_loaded_hero_data()


menu.display_beginning_image()
menu.menu()
current_hero = menu.chosen_hero


background_rect = map_controller.show_current_map().get_rect()
loading_game_screen(screen, map_controller, current_hero, background_rect)


MANA_REGEN = pygame.USEREVENT  # next event must be +1 ,because the events have ID's
pygame.time.set_timer(MANA_REGEN, 1000)

SKILL_COOLDOWN = pygame.USEREVENT + 1
pygame.time.set_timer(SKILL_COOLDOWN, 100)

death_timer = 0
clock = pygame.time.Clock()

game_running = True
while game_running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False

            if current_hero.is_attacking or current_hero.is_dead:
                continue

            elif event.key == pygame.K_1:
                hero_controller.skill_to_use = 1

            # healing spell
            elif event.key == pygame.K_2:
                hero_controller.skill_to_use = 2

            elif event.key == pygame.K_3:
                hero_controller.skill_to_use = 3

            elif event.key == pygame.K_4:
                hero_controller.skill_to_use = 4

        # calling custom event that regenerates the mana per second if the hero is not attacking
        if event.type == MANA_REGEN:
            hero_controller.mana_regen(current_hero)

        if event.type == SKILL_COOLDOWN:
            hero_controller.lower_skill_cooldown(current_hero, 0.100)
            monster_controller.lower_attack_cooldown(0.100)

    screen.blit(map_controller.show_current_map(), (0, 0))

    hero_controller.display_health_and_mana_bars(screen, current_hero)
    hero_controller.display_health_and_mana_stats(screen, current_hero)
    hero_controller.display_hero_frame_and_level(screen, current_hero)
    hero_controller.display_experience_bar(screen, current_hero)
    hero_controller.display_exp_bar_box_info(screen, current_hero, pygame.mouse.get_pos())
    hero_controller.display_keyboard_keys_below_skill_icons(screen, current_hero)

    screen.blit(action_bar_image, (action_bar_x_pos, action_bar_y_pos))
    hero_controller.display_skill_icons(screen, current_hero, action_bar_x_pos, action_bar_y_pos)
    hero_controller.show_skill_description(screen, current_hero, pygame.mouse.get_pos())

    map_controller.display_leading_arrow_on_cleared_stage(screen)

    if current_hero.is_attacking:
        screen.blit(current_hero.attack_animation(), current_hero.get_hero_pos())

    elif pygame.key.get_pressed()[pygame.K_d]:
        if not current_hero.is_right_direction:
            current_hero.change_direction()

        if not monster_controller.first_spawn:
            monster_controller.set_first_spawn()

        if not current_hero.is_dead:
            current_hero.walk()
            screen.blit(current_hero.walk_images(), current_hero.get_hero_pos())

            map_controller.check_for_traverse(current_hero, monster_controller.current_monster)

    elif pygame.key.get_pressed()[pygame.K_a]:
        if current_hero.is_right_direction:
            current_hero.change_direction()

        if not monster_controller.first_spawn:
            monster_controller.set_first_spawn()

        if not current_hero.is_dead:
            current_hero.walk()
            screen.blit(current_hero.walk_images(), current_hero.get_hero_pos())

            map_controller.check_for_traverse(current_hero, monster_controller.current_monster)

    else:
        if not current_hero.is_attacking and not current_hero.is_dead:
            screen.blit(current_hero.idle_animation(), current_hero.get_hero_pos())

    if monster_controller.first_spawn:
        map_controller.spawn_monster_on_non_cleared_stage(monster_controller.current_monster)

        hero_controller.add_enemy(monster_controller.current_monster)

        monster_controller.actions(screen, current_hero)
        monster_controller.display_health_bar(screen)

    # calling the skills animations on button press
    hero_controller.use_skill(current_hero, screen)

    if current_hero.is_dead:
        death_timer += clock.tick(60) / 1000

        if death_timer < 2.5:
            hero_controller.display_death_image(screen, current_hero)

        else:
            death_timer = 0

            menu.enter_menu_from_game_world(map_controller.show_current_map())

            menu.open_menu()
            menu.menu()

            current_hero.set_stats_for_current_level()
            current_hero = menu.chosen_hero
            current_hero.x = current_hero.start_x_pos

            monster_controller.current_monster.set_default_values_after_death()
            monster_controller.current_monster.set_max_stats_for_current_level()
            monster_controller.first_spawn = False

            map_controller.reset_cleared_stages_progress()

    pygame.display.update()

pygame.quit()

set_hero_data.save_progress_of_game()
