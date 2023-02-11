from pygame import image, transform


class Mage:

    def __init__(self, x=-30, y=300):
        self.index = 0
        self.x = x
        self.y = y

    # def idle_animation(self, direction):
    #     self.index += self.__IDLE_SPEED
    #     if direction == 'right':
    #         return idle_images_right[int(self.index) % len(idle_images_right)]
    #     return idle_images_left[int(self.index) % len(idle_images_left)]
    #
    # def walk_images(self, direction):
    #     self.index += self.__IDLE_SPEED
    #     if direction == "right":
    #         return walk_images_right[int(self.index) % len(walk_images_right)]
    #     return walk_images_left[int(self.index) % len(walk_images_left)]
    #
    # def jump_animation(self):
    #     self.index += self.__IDLE_SPEED
    #     return walk_images_right[int(self.index) % len(walk_images_right)]
    #
    # def attack_animation(self, direction):
    #     self.index += 0.1
    #     if direction == "right":
    #         return attack_images_right[int(self.index) % len(attack_images_right)]
    #     return attack_images_left[int(self.index) % len(attack_images_left)]
