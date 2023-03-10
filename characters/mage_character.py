from characters.hero import Hero
from characters.skills import BlueBall, HealAndMana, Lightning, MeteorStrike


class Mage(Hero):
    START_HEALTH = 80

    MANA_REGEN_PER_SECOND = 1

    def __init__(self, x: int, y: int, attack_images: list, die_image, idle_images: list, jump_images: list,
                 walk_images: list, profile_pic: object):
        super().__init__(x, y, self.START_HEALTH, self.START_HEALTH, attack_images, die_image, idle_images, jump_images, walk_images, profile_pic)

        self.mana_bar = self.make_bar(self.frame.width, 35, self.BAR_LENGTH, 35)

        self.max_mana = 150
        self.mana = 150

        blue_ball = BlueBall(20)
        hp_mp_gain = HealAndMana()
        lightning = Lightning(30)
        meteor_strike = MeteorStrike(40)

        self.skills = {
            1: blue_ball,
            2: hp_mp_gain,
            3: lightning,
            4: meteor_strike,
        }

    def check_mana_limit(self):
        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def receive_mana(self, amount: int or float):
        self.mana += amount
        self.check_mana_limit()

    def consume_mana_on_skill(self, amount: int or float):
        self.mana -= amount

    def check_enough_mana_to_cast(self, amount: int or float):
        return self.mana >= amount

    def increase_mana_bar_width(self, heal_power: int or float):
        self.mana_bar.width = self.increase_bar_width(self.mana, self.max_mana, heal_power)

    def decrease_mana_bar_width(self, skill_cost: int or float):
        self.mana_bar.width = self.lower_bar_width(self.mana, self.max_mana, skill_cost)
