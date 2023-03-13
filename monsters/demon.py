from monsters.monster import Monster
from pygame import image, transform


class Demon(Monster):
    IMAGE_LOOP_SPEED = 0.12
    MOVE_SPEED = 1.5

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

    def walk(self, hero_x_pos: int):
        """
        the number 120 are the empty pixels between the hero and the end of the image
        """
        self.walk_and_idle_index += Demon.IMAGE_LOOP_SPEED

        image_index = int(self.walk_and_idle_index) % len(self.walk_left)

        if self.x_pos - 120 == hero_x_pos:
            self.target_reached = True
        else:
            self.target_reached = False

        if not self.target_reached:
            if self.x_pos - 120 > hero_x_pos:
                self.x_pos -= Demon.MOVE_SPEED
                self.left_direction = True

            elif hero_x_pos > self.x_pos + 120:
                self.x_pos += Demon.MOVE_SPEED
                self.left_direction = False

        if not self.left_direction:
            return self.walk_right[image_index]
        return self.walk_left[image_index]

    def idle(self):
        self.walk_and_idle_index += Demon.IMAGE_LOOP_SPEED

        image_index = int(self.walk_and_idle_index) % len(self.idle_left)
        if self.left_direction:
            return self.idle_left[image_index]
        return self.idle_right[image_index]

    def death(self):
        pass
