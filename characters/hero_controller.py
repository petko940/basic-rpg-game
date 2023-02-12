from characters.hunter_character import Hunter
from characters.mage_character import Mage
from characters.warrior_character import Warrior
from pygame import image, transform

resized = 1.4


class HeroController:

    def __init__(self):
        self.heroes = {}

    @property
    def valid_heroes(self):
        return {"Warrior": Warrior, "Mage": Mage, "Hunter": Hunter}

    @property
    def get_load_funcs(self):
        return {"Warrior": self.load_warrior_images, "Mage": self.load_mage_images, "Hunter": self.load_hunter_images}

    def create_hero(self, hero: str, x_pos: int, y_pos: int):
        if hero in self.valid_heroes:
            loaded_images = self.get_load_funcs[hero.capitalize()]()

            new_hero = self.valid_heroes[hero.capitalize()](x_pos, y_pos, *loaded_images)

            self.heroes[hero.capitalize()] = self.heroes.get(hero.capitalize(), new_hero)

            print(f"hero of type {type(new_hero)} has been added")

    def get_hero_object(self, hero_name: str):
        return self.heroes.get(hero_name.capitalize(), "Not Found")

    @staticmethod
    def load_warrior_images():
        attack_images = [transform.scale(image.load(f'characters/war/attack/({i}).png'),
                                         (647 / resized, 633 / resized)) for i in range(1, 11)]

        die_images = [transform.scale(image.load(f'characters/war/die/({i}).png'),
                                      (668 / resized, 540 / resized)) for i in range(1, 11)]

        idle_images = [transform.scale(image.load(f'characters/war/idle/({i}).png'),
                                       (580 / resized, 520 / resized)) for i in range(1, 11)]

        jump_images = [transform.scale(image.load(f'characters/war/jump/({i}).png'),
                                       (703 / resized, 678 / resized)) for i in range(1, 11)]

        walk_images = [transform.scale(image.load(f'characters/war/walk/({i}).png'),
                                       (610 / resized, 555 / resized)) for i in range(1, 11)]

        return attack_images, die_images, idle_images, jump_images, walk_images

    @staticmethod
    def load_mage_images():
        attack_images = [transform.scale(image.load(f'characters/mage/attack/({i}).png'),()) for i in range(1, 8)]

        die_images = [transform.scale(image.load(f'characters/mage/die/({i}).png'),())  for i in range(1, 10)]

        idle_images = [transform.scale(image.load(f'characters/mage/idle/({i}).png'),())  for i in range(1, 11)]

        jump_images = [transform.scale(image.load(f'characters/mage/jump/({i}).png'),())  for i in range(1, 11)]

        walk_images = [transform.scale(image.load(f'characters/mage/walk/({i}).png'),())  for i in range(1, 11)]

        return attack_images, die_images, idle_images, jump_images, walk_images

    @staticmethod
    def load_hunter_images():
        attack_images = [image.load(f'characters/hunt/attack/({i}).png') for i in range(1, 11)]

        die_images = [image.load(f'characters/hunt/die/({i}).png') for i in range(1, 11)]

        idle_images = [image.load(f'characters/hunt/idle/({i}).png') for i in range(1, 11)]

        jump_images = [image.load(f'characters/hunt/jump/({i}).png') for i in range(1, 11)]

        walk_images = [image.load(f'characters/hunt/walk/({i}).png') for i in range(1, 11)]

        return attack_images, die_images, idle_images, jump_images, walk_images
