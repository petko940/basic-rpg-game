import pygame

from characters.hero_controller import HeroController
from menu_class import Menu
from class_maps.map_controller import MapController
from characters.actions import Actions

pygame.init()


def loading_game_screen(window, current_map: MapController, hero_actions: Actions, rect_of_background: pygame.Rect):
    for i in range(510, 0, -1):
        window.blit(current_map.show_current_map(), (0, 0))
        window.blit(current_hero.idle_animation('right'), hero_actions.idle())
        pygame.draw.rect(window, (50, (255 - i // 2), 0), rect_of_background, int(i * 1.1))
        pygame.display.update()


WIDTH, HEIGHT = (1366, 768)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
resized = 1.4


def load_mage_images():  # this func goes to hero_controller
    attack_images = [pygame.image.load(f'images/mage/attack/({i}).png') for i in range(1, 11)]

    die_images = [pygame.image.load(f'images/mage/die/({i}).png') for i in range(1, 11)]

    idle_images = [pygame.image.load(f'images/mage/idle/({i}).png') for i in range(1, 11)]

    jump_images = [pygame.image.load(f'images/mage/jump/({i}).png') for i in range(1, 11)]

    walk_images = [pygame.image.load(f'images/mage/walk/({i}).png') for i in range(1, 11)]

    return attack_images, die_images, idle_images, jump_images, walk_images


def load_hunter_images():   # this func goes to hero_controller
    attack_images = [pygame.image.load(f'images/hunt/attack/({i}).png') for i in range(1, 11)]

    die_images = [pygame.image.load(f'images/hunt/die/({i}).png') for i in range(1, 11)]

    idle_images = [pygame.image.load(f'images/hunt/idle/({i}).png') for i in range(1, 11)]

    jump_images = [pygame.image.load(f'images/hunt/jump/({i}).png') for i in range(1, 11)]

    walk_images = [pygame.image.load(f'images/hunt/walk/({i}).png') for i in range(1, 11)]

    return attack_images, die_images, idle_images, jump_images, walk_images


map_controller = MapController()
map_controller.create_map([pygame.transform.scale(pygame.image.load(f'images/maps/map1/({i}).png'), (1920 / resized, 1080 / resized)) for i in range(1, 5 + 1)], "Forest")

hero_controller = HeroController()
hero_controller.create_hero("Warrior")
# hero_controller.create_hero("Mage")  # no logic for them yet
# hero_controller.create_hero("Hunter")  # no logic for them yet


menu = Menu()
actions = Actions()

menu.menu()   # must pass objects to this object so that we can see them in the menu
current_hero = menu.chosen_hero

background_rect = map_controller.show_current_map().get_rect()

loading_game_screen(screen, map_controller, actions, background_rect)


is_right = True
game_running = True
while game_running:
    pygame.time.Clock().tick(100)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            # elif event.key == pygame.K_d:
            #     screen.blit(warrior.walk_images("right"),warrior.idle_animation("right").get_rect())
            # TO DO walk right
            # char.walking = True

    screen.blit(map_controller.show_current_map(), (0, 0))

    if pygame.key.get_pressed()[pygame.K_d] and pygame.key.get_pressed()[pygame.K_SPACE]:
        screen.blit(current_hero.walk_images("right"), actions.walk())
        screen.blit(current_hero.attack_animation("right"), actions.attack())

    elif pygame.key.get_pressed()[pygame.K_d]:
        screen.blit(current_hero.walk_images("right"), actions.walk())
        if actions.check_for_traverse():
            map_controller.traverse_image()
        is_right = True

    elif pygame.key.get_pressed()[pygame.K_a]:
        screen.blit(current_hero.walk_images("left"), actions.walk())
        is_right = False

    elif pygame.key.get_pressed()[pygame.K_SPACE]:
        screen.blit(current_hero.attack_animation("right"), actions.attack())

    else:
        print(current_hero.idle_animation('right').get_rect())
        if is_right:
            screen.blit(current_hero.idle_animation('right'), actions.idle())
        else:
            screen.blit(current_hero.idle_animation('left'), actions.idle())
    pygame.display.update()

pygame.quit()
