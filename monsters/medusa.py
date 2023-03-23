from monsters.monster import Monster
from pygame import image, transform, Rect


class Medusa(Monster):
    IMAGE_LOOP_SPEED = 0.12
    MOVE_SPEED = 2
    ATK_SPEED = 0.12

    LOWER_HIT_BOX = 120

    ATTACK_COOLDOWN = 2

    def __init__(self, health: int, damage: int, x_pos: int, y_pos: int):
        super().__init__(health, damage, x_pos, y_pos)

        self.attack_right = [transform.scale(image.load(f'monsters/medusa_sprites/attack/{i}.png'), (293, 276)) for i in range(6)]
        self.attack_left = [transform.flip(self.attack_right[i], True, False) for i in range(len(self.attack_right))]

        self.die_right = [transform.scale(image.load(f'monsters/medusa_sprites/death/{i}.png'), (293, 276)) for i in range(6)]
        self.die_left = [transform.flip(self.die_right[i], True, False) for i in range(len(self.die_right))]

        self.idle_right = [transform.scale(image.load(f'monsters/medusa_sprites/idle/{i}.png'), (293, 276)) for i in range(3)]
        self.idle_left = [transform.flip(self.idle_right[i], True, False) for i in range(len(self.idle_right))]

        self.walk_right = [transform.scale(image.load(f'monsters/medusa_sprites/walk/{i}.png'), (293, 276)) for i in range(4)]
        self.walk_left = [transform.flip(self.walk_right[i], True, False) for i in range(len(self.walk_right))]

        self.rect_image = self.attack_left[0].get_rect()

    @property
    def rect_hit_box(self):
        if self.left_direction:
            return Rect(self.x_pos + Medusa.LOWER_HIT_BOX, self.y_pos + 30, self.rect_image.width - Medusa.LOWER_HIT_BOX, self.rect_image.height)
        return Rect(self.x_pos, self.y_pos + 30, self.rect_image.width - Medusa.LOWER_HIT_BOX, self.rect_image.height)

    def increase_index_attack_animation(self):
        self.non_looped_index += Medusa.ATK_SPEED

    def check_end_of_attack(self):
        if int(self.non_looped_index) >= len(self.attack_left):
            self.is_attacking = False
            self.attack_cooldown = Medusa.ATTACK_COOLDOWN
            self.non_looped_index = 0

    def check_target_reached(self, hero):
        difference_left = abs((self.x_pos - Medusa.LOWER_HIT_BOX) - hero.x)
        difference_right = abs((self.x_pos + Medusa.LOWER_HIT_BOX) - hero.x)

        if difference_left < 80 or difference_right < 80 or difference_left + difference_right == Medusa.LOWER_HIT_BOX * 2:
            return True
        return False

    def walk(self, hero_x_pos: int):
        self.walk_and_idle_index += Medusa.IMAGE_LOOP_SPEED

        image_index = int(self.walk_and_idle_index) % len(self.walk_left)

        if self.x_pos - Medusa.LOWER_HIT_BOX > hero_x_pos:
            self.x_pos -= Medusa.MOVE_SPEED
            self.health_bar.x -= Medusa.MOVE_SPEED
            self.background_health_bar.x -= Medusa.MOVE_SPEED
            self.left_direction = True

        elif hero_x_pos > self.x_pos + Medusa.LOWER_HIT_BOX:
            self.x_pos += Medusa.MOVE_SPEED
            self.health_bar.x += Medusa.MOVE_SPEED
            self.background_health_bar.x += Medusa.MOVE_SPEED
            self.left_direction = False

        return self.get_image(image_index, self.walk_left, self.walk_right)

    def idle(self):
        self.walk_and_idle_index += Medusa.IMAGE_LOOP_SPEED

        image_index = int(self.walk_and_idle_index) % len(self.idle_left)

        return self.get_image(image_index, self.idle_left, self.idle_right)

    def increase_death_image_index(self):
        self.non_looped_index += Medusa.IMAGE_LOOP_SPEED

    def death(self):
        return self.get_image(int(self.non_looped_index), self.die_left, self.die_right)

    def health_bar_position(self):
        if self.left_direction:
            return self.health_bar.x + 130, self.y_pos, self.health_bar.width, self.HEALTH_BAR_HEIGHT
        return self.health_bar.x + 60, self.y_pos, self.health_bar.width, self.HEALTH_BAR_HEIGHT

    def health_bar_pad_position(self):
        if self.left_direction:
            return self.background_health_bar.x + 130, self.y_pos, self.background_health_bar.width, self.HEALTH_BAR_HEIGHT
        return self.background_health_bar.x + 60, self.y_pos, self.background_health_bar.width, self.HEALTH_BAR_HEIGHT
