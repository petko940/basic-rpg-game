from pygame import transform, Rect, Surface


class Hero:
    __IDLE_SPEED = 0.25
    __ATK_SPEED = 0.2
    __MOVE_SPEED = 5
    BAR_LENGTH = 275

    def __init__(self, x: int, y: int, health: int, max_health: int, attack_images: list, die_image: Surface, idle_images: list,
                 jump_images: list, walk_images: list, profile_pic: object):
        self.x = x
        self.y = y
        self.level = 1

        self.max_health = max_health
        self.health = health

        self.attack_images_right = attack_images
        self.attack_images_left = [transform.flip(self.attack_images_right[i], True, False) for i in range(len(self.attack_images_right))]

        self.die_image = die_image

        self.idle_images_right = idle_images
        self.idle_images_left = [transform.flip(self.idle_images_right[i], True, False) for i in range((len(self.idle_images_right)))]

        self.jump_images = jump_images

        self.walk_images_right = walk_images
        self.walk_images_left = [transform.flip(self.walk_images_right[i], True, False) for i in range(len(self.walk_images_right))]

        self.profile_pic = profile_pic  # Surface object

        self.idle_index = 0
        self.on_press_index = 0

        self.is_attacking = False

        self.frame = self.make_bar(0, 0, 70, 70)

        self.health_bar = self.make_bar(self.frame.width, 0, self.BAR_LENGTH, 35)

        self.background_rect_health_bar = self.make_bar(self.frame.width, 0, self.BAR_LENGTH, 35)
        self.background_rect_mana_bar = self.make_bar(self.frame.width, 35, self.BAR_LENGTH, 35)

    @staticmethod
    def make_bar(x, y, width, height):
        return Rect(x, y, width, height)

    def lower_bar_width(self, current_value: int or float, max_value: int or float, extract_value: int or float):
        bar_width = self.BAR_LENGTH * ((current_value - extract_value) / max_value)

        if bar_width > self.BAR_LENGTH:
            return self.BAR_LENGTH
        return bar_width

    def increase_bar_width(self, current_value: int or float, max_value: int or float, add_value: int or float):
        bar_width = self.BAR_LENGTH * ((current_value + add_value) / max_value)

        if bar_width > self.BAR_LENGTH:
            return self.BAR_LENGTH
        return bar_width

    def check_health_limit(self):
        if self.health > self.max_health:
            self.health = self.max_health

    def receive_healing(self, amount: int or float):
        self.health += amount
        self.check_health_limit()

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