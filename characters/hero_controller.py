from characters.hunter_character import Hunter
from characters.mage_character import Mage
from characters.warrior_character import Warrior
from pygame import image, transform

resized = 1.4


class HeroController:

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
            hero.health_bar = hero.lower_bar_width(hero.health_bar, hero.health, hero.max_health, monster.damage)

    @staticmethod
    def check_if_hero_died(hero: object) -> bool:
        """
        returns True if the width of the health_bar is less than or equal to zero, otherwise returns False
        """
        return hero.health_bar.width <= 0

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
        attack_images = [
            transform.scale(image.load(f'characters/mage/attack/({i}).png'), (466 / resized, 561 / resized)) for i in
            range(1, 8)]

        die_images = [transform.scale(image.load(f'characters/mage/die/({i}).png'), (671 / resized, 550 / resized)) for
                      i in range(1, 10)]

        idle_images = [transform.scale(image.load(f'characters/mage/idle/({i}).png'), (466 / resized, 535 / resized))
                       for i in range(1, 11)]

        jump_images = [transform.scale(image.load(f'characters/mage/jump/({i}).png'), (478 / resized, 675 / resized))
                       for i in range(1, 11)]

        walk_images = [transform.scale(image.load(f'characters/mage/walk/({i}).png'), (467 / resized, 561 / resized))
                       for i in range(1, 11)]

        return attack_images, die_images, idle_images, jump_images, walk_images

    @staticmethod
    def load_hunter_images():
        attack_images = [image.load(f'characters/hunt/attack/({i}).png') for i in range(1, 11)]

        die_images = [image.load(f'characters/hunt/die/({i}).png') for i in range(1, 11)]

        idle_images = [transform.scale(image.load(f'characters/hunt/idle/({i}).png'), (483 / resized, 550 / resized))
                       for i in range(1, 11)]

        jump_images = [image.load(f'characters/hunt/jump/({i}).png') for i in range(1, 11)]

        walk_images = [image.load(f'characters/hunt/walk/({i}).png') for i in range(1, 11)]

        return attack_images, die_images, idle_images, jump_images, walk_images
