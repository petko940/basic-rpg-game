from characters.hunter_character import Hunter
from characters.mage_character import Mage
from characters.warrior_character import Warrior
import pygame

pygame.font.init()

resized = 1.4

font = pygame.font.SysFont('Cosmic Sans bold', 40)


class HeroController:
    HEALTH_BAR_COLOR = (180, 0, 0)
    MANA_BAR_COLOR = (0, 0, 220)
    BACKGROUND_BAR_COLOR = (105, 105, 105)
    FONT_COLOR = (255, 255, 255)

    def __init__(self):
        self.heroes: dict[str, object] = {}

    @property
    def valid_heroes(self):
        return {"Warrior": Warrior, "Mage": Mage, "Hunter": Hunter}

    @property
    def get_load_funcs(self):
        return {"Warrior": self.load_warrior_images, "Mage": self.load_mage_images, "Hunter": self.load_hunter_images}

    def create_hero(self, hero_type: str, x_pos: int, y_pos: int):
        if hero_type in self.valid_heroes:
            loaded_images = self.get_load_funcs[hero_type.capitalize()]()

            new_hero = self.valid_heroes[hero_type.capitalize()](x_pos, y_pos, *loaded_images)

            self.heroes[hero_type.capitalize()] = self.heroes.get(hero_type.capitalize(), new_hero)

            print(f"hero of type {type(new_hero)} has been added")

    def get_hero_object(self, hero_name: str):
        """
        returns hero as object and if not found, returns "Not Found"
        """
        return self.heroes.get(hero_name.capitalize(), "Not Found")

    def take_damage(self, hero: object, monster: object) -> None:
        # this method is not working since there are still NO monster objects
        """
        Gets the hero health_bar and goes into the method (lower bar width) which is inside the Hero class.
        lower_bar_width returns the new health_bar width and take_damage method applies the changes
        THIS METHOD must be used hand by hand with check_if_hero_died
        """
        if hero in self.heroes.values():
            hero.health_bar.width = hero.lower_bar_width(hero.health, hero.max_health, monster.damage) # NOQA
            if hero.health > 0:
                hero.health -= monster.damage

    def display_bars(self, screen, hero: object):
        pygame.draw.rect(screen, self.BACKGROUND_BAR_COLOR, hero.background_rect_health_bar)
        pygame.draw.rect(screen, self.HEALTH_BAR_COLOR, hero.health_bar)
        if type(hero).__name__ != "Warrior":
            pygame.draw.rect(screen, self.BACKGROUND_BAR_COLOR, hero.background_rect_mana_bar)
            pygame.draw.rect(screen, self.MANA_BAR_COLOR, hero.mana_bar)

    @staticmethod
    def check_if_hero_died(hero: object) -> bool:
        """
        returns True if the health is less than or equal to zero, otherwise returns False
        """
        return hero.health <= 0

    def display_health_and_mana_stats(self, screen, hero: object):
        health_surface = font.render(f"{hero.health}/{hero.max_health}", True, self.FONT_COLOR)

        middle_of_hp_bar = (hero.BAR_LENGTH // 2) - (health_surface.get_rect().width // 2)

        screen.blit(health_surface, (middle_of_hp_bar, 5))
        if type(hero).__name__ != "Warrior":
            mana_surface = font.render(f"{hero.mana}/{hero.max_mana}", True, self.FONT_COLOR)

            middle_of_mana_bar = (hero.BAR_LENGTH // 2) - (mana_surface.get_rect().width // 2)

            screen.blit(mana_surface, (middle_of_mana_bar, 40))

    def display_hero_frame_and_level(self, screen, hero: object):
        """
        must draw a frame (with code) and add the picture of the current hero inside
        must cut 3 pictures (head of war, mage and hunter)
        must display current level too
        """
        ...

    @staticmethod
    def load_warrior_images():
        attack_images = [pygame.transform.scale(pygame.image.load(f'characters/war/attack/({i}).png'),
                                         (647 / resized, 633 / resized)) for i in range(1, 11)]

        die_images = [pygame.transform.scale(pygame.image.load(f'characters/war/die/({i}).png'),
                                      (668 / resized, 540 / resized)) for i in range(1, 11)]

        idle_images = [pygame.transform.scale(pygame.image.load(f'characters/war/idle/({i}).png'),
                                       (580 / resized, 520 / resized)) for i in range(1, 11)]

        jump_images = [pygame.transform.scale(pygame.image.load(f'characters/war/jump/({i}).png'),
                                       (703 / resized, 678 / resized)) for i in range(1, 11)]

        walk_images = [pygame.transform.scale(pygame.image.load(f'characters/war/walk/({i}).png'),
                                       (610 / resized, 555 / resized)) for i in range(1, 11)]

        return attack_images, die_images, idle_images, jump_images, walk_images

    @staticmethod
    def load_mage_images():
        attack_images = [
            pygame.transform.scale(pygame.image.load(f'characters/mage/attack/({i}).png'), (466 / resized, 561 / resized)) for i in
            range(1, 8)]

        die_images = [pygame.transform.scale(pygame.image.load(f'characters/mage/die/({i}).png'), (671 / resized, 550 / resized)) for
                      i in range(1, 10)]

        idle_images = [pygame.transform.scale(pygame.image.load(f'characters/mage/idle/({i}).png'), (466 / resized, 535 / resized))
                       for i in range(1, 11)]

        jump_images = [pygame.transform.scale(pygame.image.load(f'characters/mage/jump/({i}).png'), (478 / resized, 675 / resized))
                       for i in range(1, 11)]

        walk_images = [pygame.transform.scale(pygame.image.load(f'characters/mage/walk/({i}).png'), (467 / resized, 561 / resized))
                       for i in range(1, 11)]

        return attack_images, die_images, idle_images, jump_images, walk_images

    @staticmethod
    def load_hunter_images():
        attack_images = [pygame.image.load(f'characters/hunt/attack/({i}).png') for i in range(1, 11)]

        die_images = [pygame.image.load(f'characters/hunt/die/({i}).png') for i in range(1, 11)]

        idle_images = [pygame.transform.scale(pygame.image.load(f'characters/hunt/idle/({i}).png'), (483 / resized, 550 / resized))
                       for i in range(1, 11)]

        jump_images = [pygame.image.load(f'characters/hunt/jump/({i}).png') for i in range(1, 11)]

        walk_images = [pygame.image.load(f'characters/hunt/walk/({i}).png') for i in range(1, 11)]

        return attack_images, die_images, idle_images, jump_images, walk_images
