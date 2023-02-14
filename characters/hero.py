from pygame import transform, Rect


class Hero:
    __MAP_WIDTH = 1366
    __IDLE_SPEED = 0.25
    __ATK_SPEED = 0.2
    __MOVE_SPEED = 5
    BAR_LENGTH = 300

    def __init__(self, x: int, y: int, attack_images: list, die_images: list, idle_images: list,
                 jump_images: list, walk_images: list):
        self.x = x
        self.y = y
        self.level = 1

        self.attack_images_right = attack_images
        self.attack_images_left = [transform.flip(self.attack_images_right[i], True, False) for i in range(len(self.attack_images_right))]

        self.die_images_right = die_images
        self.die_images_left = [transform.flip(self.die_images_right[i], True, False) for i in range(len(self.die_images_right))]

        self.idle_images_right = idle_images
        self.idle_images_left = [transform.flip(self.idle_images_right[i], True, False) for i in range((len(self.idle_images_right)))]

        self.jump_images = jump_images

        self.walk_images_right = walk_images
        self.walk_images_left = [transform.flip(self.walk_images_right[i], True, False) for i in range(len(self.walk_images_right))]

        self.idle_index = 0
        self.on_press_index = 0

        self.is_attacking = False

        self.health_bar = self.make_bar(0, 0, self.BAR_LENGTH, 35)

    @staticmethod
    def make_bar(x, y, width, height):
        return Rect(x, y, width, height)

    def idle_animation(self, direction: str):
        self.idle_index += self.__IDLE_SPEED
        if direction == "right":
            return self.idle_images_right[int(self.idle_index) % len(self.idle_images_right)]
        return self.idle_images_left[int(self.idle_index) % len(self.idle_images_left)]

    def walk_images(self, direction: str):
        self.idle_index += self.__IDLE_SPEED
        if direction == "right":
            return self.walk_images_right[int(self.idle_index) % len(self.walk_images_right)]
        return self.walk_images_left[int(self.idle_index) % len(self.walk_images_left)]

    def attack_animation(self, direction: str):
        self.on_press_index += self.__ATK_SPEED

        if self.on_press_index >= len(self.attack_images_right):
            self.is_attacking = False
            self.on_press_index = 0

        if direction == "right":
            return self.attack_images_right[int(self.on_press_index)]
        return self.attack_images_left[int(self.on_press_index)]

    def jump_animation(self):
        self.idle_index += self.__IDLE_SPEED
        return self.jump_images[int(self.idle_index) % len(self.jump_images)]

    def check_for_traverse(self):
        if self.x >= self.__MAP_WIDTH - 150:
            self.x = -30
            return True

    def walk(self, direction: str):
        if direction == 'right':
            self.x += self.__MOVE_SPEED

        else:
            self.x -= self.__MOVE_SPEED

        return self.x, self.y

    def idle(self):
        return self.x, self.y

    def attack(self):
        return self.x, self.y