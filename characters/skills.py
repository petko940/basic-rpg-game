from abc import ABC
from pygame import transform, image


class Skill(ABC):
    MAP_WIDTH = 1366

    def __init__(self, skill_cost: int, level_required: int):
        self.skill_cost = skill_cost
        self.level_required = level_required
        self.text_box = image.load('characters/skill_info_box/info_text_box.png')
        self.is_animating = False


class BlueBall(Skill):
    BALL_SPEED = 9
    DAMAGE_INCREASE = 5
    LEVEL_REQUIRED = 1

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/mage/blue_ball_skill_image.png')
        self.images_right = [image.load(f'characters/mage/blue_ball_sprites/{i}.png') for i in range(1, 6 + 1)]
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
        self.damage += self.DAMAGE_INCREASE


class HealAndMana(Skill):
    LEVEL_REQUIRED = 2

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/mage/hp_mp_gain.png')
        self.healing = 25

    def heal(self):
        return self.healing

    def level_up(self):
        self.healing += 10


class AxeBasicAttack(Skill):
    DAMAGE_INCREASE = 5
    LEVEL_REQUIRED = 1

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/war/axe_basic_attack.png')
        self.damage = 25

    def level_up(self):
        self.damage += self.DAMAGE_INCREASE


class Heal(Skill):
    HEAL_INCREASE = 5
    LEVEL_REQUIRED = 1

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/war/heal.png')
        self.healing = 25

    def heal(self):
        return self.healing

    def level_up(self):
        self.healing += self.HEAL_INCREASE