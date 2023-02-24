from abc import ABC, abstractmethod
from pygame import transform, image


class Skill(ABC):
    MAP_WIDTH = 1366

    def __init__(self, skill_cost: int, level_required: int):
        self.skill_cost = skill_cost
        self.level_required = level_required
        self.text_box = image.load('characters/skill_info_box/info_text_box.png')
        self.is_animating = False

    @abstractmethod
    def get_description(self):
        pass


class BlueBall(Skill):
    BALL_SPEED = 9
    DAMAGE_INCREASE_PER_LEVEL = 5
    LEVEL_REQUIRED = 1

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/mage/blue_ball_skill_image.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.images_right = [image.load(f'characters/mage/skill_animations/blue_ball_sprites/{i}.png') for i in range(1, 6 + 1)]
        self.images_left = [transform.flip(self.images_right[i], True, False) for i in range(len(self.images_right))]
        self.x_pos = 0
        self.img_index = 0
        self.damage = 25

    def cast_ball(self):
        if not self.is_animating:
            self.is_animating = True

    def animating_the_ball(self):
        if self.is_animating:
            self.x_pos += self.BALL_SPEED
            self.img_index += 0.2

            return self.images_right[int(self.img_index) % len(self.images_right)]

    def check_for_end_point(self):
        if self.x_pos > self.MAP_WIDTH + self.images_right[0].get_rect().width:
            self.reset_skill_position()

    def reset_skill_position(self):
        self.x_pos = 0
        self.img_index = 0
        self.is_animating = False

    def level_up(self):
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Blue Ball",
                f"Cost: {self.skill_cost}",
                f"Damage: {self.damage}"
                ]


class HealAndMana(Skill):
    LEVEL_REQUIRED = 2
    HEAL_MANA_INCREASE_PER_LEVEL = 10

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/mage/hp_mp_gain.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.healing = 25

    def heal(self):
        return self.healing

    def level_up(self):
        self.healing += self.HEAL_MANA_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Heal and Mana",
                f"Cost: {self.skill_cost}",
                f"Heal power: {self.healing}",
                f"Mana gain: {self.healing}"
                ]


class Lightning(Skill):
    LEVEL_REQUIRED = 3
    DAMAGE_INCREASE_PER_LEVEL = 10

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/mage/thunderstorm_skill_icon.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.images = [image.load(f'characters/mage/skill_animations/thunder_sprites/{x}.png') for x in range(1, 9 + 1)]
        self.img_index = 0
        self.damage = 30

    def level_up(self):
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Lightning",
                f"Cost: {self.skill_cost}",
                f"Damage: {self.damage}"
                ]


class AxeBasicAttack(Skill):
    DAMAGE_PER_LEVEL_INCREASE = 5
    LEVEL_REQUIRED = 1

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/war/axe_basic_attack.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.damage = 25

    def level_up(self):
        self.damage += self.DAMAGE_PER_LEVEL_INCREASE

    def get_description(self):
        return ["Axe Attack",
                f"Cost: {self.skill_cost}",
                f"Damage: {self.damage}"]


class Heal(Skill):
    HEAL_INCREASE_PER_LEVEL = 5
    LEVEL_REQUIRED = 1

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/war/heal.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.healing = 25

    def heal(self):
        return self.healing

    def level_up(self):
        self.healing += self.HEAL_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Heal",
                f"Cost: {self.skill_cost}",
                f"Heal power: {self.healing}"
                ]
