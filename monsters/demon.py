from monsters.monster import Monster
from pygame import image, transform


class Demon(Monster):
    IMAGE_LOOP_SPEED = 0.12
    MOVE_SPEED = 2

    def __init__(self, health: int, x_pos: int, y_pos: int):
        super().__init__(health, x_pos, y_pos)

        self.attack_left = [transform.scale(image.load(f'monsters/demon_sprites/attack/{i}.png'), (338, 325)) for i in range(4)]
        self.attack_right = [transform.flip(self.attack_left[i], True, False) for i in range(len(self.attack_left))]

        self.die_left = [transform.scale(image.load(f'monsters/demon_sprites/death/{i}.png'), (338, 325)) for i in range(6)]
        self.die_right = [transform.flip(self.die_left[i], True, False) for i in range(len(self.die_left))]

        self.idle_left = [transform.scale(image.load(f'monsters/demon_sprites/idle/{i}.png'), (338, 325)) for i in range(3)]
        self.idle_right = [transform.flip(self.idle_left[i], True, False) for i in range(len(self.idle_left))]

        self.walk_left = [transform.scale(image.load(f'monsters/demon_sprites/walk/{i}.png'), (338, 325)) for i in range(6)]
        self.walk_right = [transform.flip(self.walk_left[i], True, False) for i in range(len(self.walk_left))]

    def attack(self):
        pass

    def check_target_reached(self, hero_x_pos: int):
        difference_left = abs((self.x_pos - 120) - hero_x_pos)
        difference_right = abs((self.x_pos + 120) - hero_x_pos)

        if difference_left < 5 or difference_right < 5:
            self.target_reached = True
        else:
            self.target_reached = False

    def walk(self, hero_x_pos: int):
        """
        the number 120 are the empty pixels between the hero and the end of the image
        """
        self.walk_and_idle_index += Demon.IMAGE_LOOP_SPEED

        image_index = int(self.walk_and_idle_index) % len(self.walk_left)

        self.check_target_reached(hero_x_pos)

        if not self.target_reached:
            if self.x_pos - 120 > hero_x_pos:
                self.x_pos -= Demon.MOVE_SPEED
                self.left_direction = True

            elif hero_x_pos > self.x_pos + 120:
                self.x_pos += Demon.MOVE_SPEED
                self.left_direction = False

        return self.get_image(image_index, self.walk_left, self.walk_right)

    def idle(self):
        self.walk_and_idle_index += Demon.IMAGE_LOOP_SPEED

        image_index = int(self.walk_and_idle_index) % len(self.idle_left)

        return self.get_image(image_index, self.idle_left, self.idle_right)

    def death(self):
        pass

    def get_image(self, index: int, images_left: list, images_right: list):
        if self.left_direction:
            return images_left[index]
        return images_right[index]