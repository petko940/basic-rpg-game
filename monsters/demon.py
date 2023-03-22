from monsters.monster import Monster
from pygame import image, transform, Rect


class Demon(Monster):
    IMAGE_LOOP_SPEED = 0.12
    MOVE_SPEED = 2
    ATK_SPEED = 0.12

    LOWER_HIT_BOX = 120

    ATTACK_COOLDOWN = 2

    def __init__(self, health: int, damage: int, x_pos: int, y_pos: int):
        super().__init__(health, damage, x_pos, y_pos)

        self.attack_left = [transform.scale(image.load(f'monsters/demon_sprites/attack/{i}.png'), (338, 325)) for i in range(4)]
        self.attack_right = [transform.flip(self.attack_left[i], True, False) for i in range(len(self.attack_left))]

        self.die_left = [transform.scale(image.load(f'monsters/demon_sprites/death/{i}.png'), (338, 325)) for i in range(6)]
        self.die_right = [transform.flip(self.die_left[i], True, False) for i in range(len(self.die_left))]

        self.idle_left = [transform.scale(image.load(f'monsters/demon_sprites/idle/{i}.png'), (338, 325)) for i in range(3)]
        self.idle_right = [transform.flip(self.idle_left[i], True, False) for i in range(len(self.idle_left))]

        self.walk_left = [transform.scale(image.load(f'monsters/demon_sprites/walk/{i}.png'), (338, 325)) for i in range(6)]
        self.walk_right = [transform.flip(self.walk_left[i], True, False) for i in range(len(self.walk_left))]

        self.rect_image = self.attack_left[0].get_rect()

    @property
    def rect_hit_box(self):
        if self.left_direction:
            return Rect(self.x_pos + Demon.LOWER_HIT_BOX, self.y_pos + 30, self.rect_image.width - Demon.LOWER_HIT_BOX, self.rect_image.height)
        return Rect(self.x_pos, self.y_pos + 30, self.rect_image.width - Demon.LOWER_HIT_BOX, self.rect_image.height)

    def attack(self):
        if not self.attack_cooldown and not self.is_attacking:
            self.is_attacking = True

    def increase_index_attack_animation(self):
        self.non_looped_index += Demon.ATK_SPEED

    def check_end_of_attack(self):
        if int(self.non_looped_index) >= len(self.attack_left):
            self.is_attacking = False
            self.attack_cooldown = Demon.ATTACK_COOLDOWN
            self.non_looped_index = 0

    def check_target_reached(self, hero):
        difference_left = abs((self.x_pos - Demon.LOWER_HIT_BOX) - hero.x)
        difference_right = abs((self.x_pos + Demon.LOWER_HIT_BOX) - hero.x)

        if difference_left < 5 or difference_right < 5 or difference_left + difference_right == Demon.LOWER_HIT_BOX * 2:
            return True
        return False

    def walk(self, hero_x_pos: int):
        self.walk_and_idle_index += Demon.IMAGE_LOOP_SPEED

        image_index = int(self.walk_and_idle_index) % len(self.walk_left)

        if self.x_pos - Demon.LOWER_HIT_BOX > hero_x_pos:
            self.x_pos -= Demon.MOVE_SPEED
            self.health_bar.x -= Demon.MOVE_SPEED
            self.background_health_bar.x -= Demon.MOVE_SPEED
            self.left_direction = True

        elif hero_x_pos > self.x_pos + Demon.LOWER_HIT_BOX:
            self.x_pos += Demon.MOVE_SPEED
            self.health_bar.x += Demon.MOVE_SPEED
            self.background_health_bar.x += Demon.MOVE_SPEED
            self.left_direction = False

        return self.get_image(image_index, self.walk_left, self.walk_right)

    def idle(self):
        self.walk_and_idle_index += Demon.IMAGE_LOOP_SPEED

        image_index = int(self.walk_and_idle_index) % len(self.idle_left)

        return self.get_image(image_index, self.idle_left, self.idle_right)

    def increase_death_image_index(self):
        self.non_looped_index += Demon.IMAGE_LOOP_SPEED

    def death(self):
        return self.get_image(int(self.non_looped_index), self.die_left, self.die_right)

    def get_image(self, index: int, images_left: list, images_right: list):
        if self.left_direction:
            return images_left[index]
        return images_right[index]

    def health_bar_position(self):
        if self.left_direction:
            return self.health_bar.x + 200, self.y_pos + 30, self.health_bar.width, self.HEALTH_BAR_HEIGHT
        return self.health_bar.x, self.y_pos + 30, self.health_bar.width, self.HEALTH_BAR_HEIGHT

    def health_bar_pad_position(self):
        if self.left_direction:
            return self.background_health_bar.x + 200, self.y_pos + 30, self.background_health_bar.width, self.HEALTH_BAR_HEIGHT
        return self.background_health_bar.x, self.y_pos + 30, self.background_health_bar.width, self.HEALTH_BAR_HEIGHT
