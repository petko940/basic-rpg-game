from characters.hero import Hero
from characters.skills import HealAndMana


class Hunter(Hero):

    def __init__(self, x: int, y: int, attack_images: list, die_images: list, idle_images: list, jump_images: list,
                 walk_images: list, profile_pic: object):
        super().__init__(x, y, attack_images, die_images, idle_images, jump_images, walk_images, profile_pic)

        self.mana_bar = self.make_bar(self.frame.width, 35, self.BAR_LENGTH, 35)

        self.max_health = 100
        self.health = 100

        self.max_mana = 80
        self.mana = 80

        hp_mp_gain = HealAndMana()

        self.skills = {
            1: 'first skill',
            2: hp_mp_gain,
            3: 'third skill',
            4: 'fourth skill'
        }