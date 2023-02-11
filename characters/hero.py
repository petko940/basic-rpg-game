from pygame import transform


class Hero:
    __IDLE_SPEED = 0.16
    __ATK_SPEED = 0.2

    def __init__(self, x: int, y: int, attack_images: list, die_images: list, idle_images: list,
                 jump_images: list, walk_images: list):
        self.x = x
        self.y = y

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

        self.is_animating = False

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
        if not self.is_animating:
            self.is_animating = True
            self.on_press_index += self.__ATK_SPEED

            if self.on_press_index >= len(self.attack_images_right):
                self.is_animating = False
                self.on_press_index = 0

            else:
                if direction == "right":
                    return self.attack_images_right[int(self.on_press_index)]
                return self.attack_images_left[int(self.on_press_index)]

    def jump_animation(self):
        self.idle_index += self.__IDLE_SPEED
        return self.jump_images[int(self.idle_index) % len(self.jump_images)]
