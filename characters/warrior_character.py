from characters.hero import Hero
from characters.skills import AxeBasicAttack, Heal, DamageBoost, PassiveCrit


class Warrior(Hero):
    START_HEALTH = 150

    def __init__(self, x: int, y: int, attack_images: list, die_image, idle_images: list, jump_images: list,
                 walk_images: list, profile_pic: object):
        super().__init__(x, y, self.START_HEALTH, self.START_HEALTH, attack_images, die_image, idle_images, jump_images, walk_images, profile_pic)

        axe_basic_attack = AxeBasicAttack()
        heal = Heal()
        damage_boost = DamageBoost()
        passive_crit = PassiveCrit()

        self.skills = {
            1: axe_basic_attack,
            2: heal,
            3: damage_boost,
            4: passive_crit
        }