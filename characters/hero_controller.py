from characters.hunter_character import Hunter
from characters.mage_character import Mage
from characters.warrior_character import Warrior
from pygame import image, transform

resized = 1.4


class HeroController:

    def __init__(self):
        self.heroes = []

    @property
    def valid_heroes(self):
        return {"Warrior": Warrior, "Mage": Mage, "Hunter": Hunter}

    @property
    def get_load_funcs(self):
        return {"Warrior": self.load_warrior_images, "Mage": Mage, "Hunter": Hunter}  # to do ... make static funcs for rest

    def create_hero(self, hero: str):
        if hero in self.valid_heroes:
            loaded_images = self.get_load_funcs[hero]()

            new_hero = self.valid_heroes[hero.capitalize()](100, 100, *loaded_images)
            self.heroes.append(new_hero)

            print(f"hero of type {type(new_hero)} has been added")

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


    # to do ... add 2 more methods
