from characters.hero import Hero
from characters.skills import HealAndMana, ArrowRain, ArrowShot, RapidShot


class Hunter(Hero):
    START_HEALTH = 100

    MANA_REGEN_PER_SECOND = 1

    HEALTH_INCREASE_PER_LEVEL = 40
    MANA_INCREASE_PER_LEVEL = 25

    def __init__(self, x: int, y: int, attack_images: list, die_image, idle_images: list, jump_images: list,
                 walk_images: list, profile_pic: object):
        super().__init__(x, y, self.START_HEALTH, self.START_HEALTH, attack_images, die_image, idle_images, jump_images, walk_images, profile_pic)

        self.mana_bar = self.make_bar(self.frame.width, 35, self.BAR_LENGTH, 35)

        self.max_mana = 80
        self.mana = 80

        arrow_shot = ArrowShot(5)
        hp_mp_gain = HealAndMana()
        rapid_shot = RapidShot(10)
        arrow_rain = ArrowRain(40)

        self.skills = {
            1: arrow_shot,
            2: hp_mp_gain,
            3: rapid_shot,
            4: arrow_rain
        }

    def set_stats_for_current_level(self):
        self.health = self.max_health
        self.mana = self.max_mana
        self.health_bar.width = self.BAR_LENGTH
        self.mana_bar.width = self.BAR_LENGTH

    def get_stronger_after_level_up(self):
        self.max_health += self.HEALTH_INCREASE_PER_LEVEL
        self.health = self.max_health
        self.max_mana += self.MANA_INCREASE_PER_LEVEL
        self.mana = self.max_mana
        self.health_bar.width = self.BAR_LENGTH
        self.mana_bar.width = self.BAR_LENGTH
        for skill in self.skills.values():
            if self.level >= skill.LEVEL_REQUIRED:
                skill.level_up()

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
        self.mana_bar.width = self.increase_bar_width(self.mana, self.max_mana, heal_power, self.BAR_LENGTH)

    def decrease_mana_bar_width(self, skill_cost: int or float):
        self.mana_bar.width = self.lower_bar_width(self.mana, self.max_mana, skill_cost)
