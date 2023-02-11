import pygame

idle_images_right = [pygame.image.load(f'images/mage/idle/({i}).png') for i in range(1, 11)]
idle_images_left = [pygame.transform.flip(idle_images_right[i], True, False) for i in range(10)]

attack_images_right = [pygame.image.load(f'images/mage/attack/({i}).png') for i in range(1, 11)]
attack_images_left = [pygame.transform.flip(attack_images_right[i], True, False) for i in range(10)]

die_images = [pygame.image.load(f'images/mage/die/({i}).png') for i in range(1, 11)]

walk_images_right = [pygame.image.load(f'images/mage/walk/({i}).png') for i in range(1, 11)]
walk_images_left = [pygame.transform.flip(walk_images_right[i], True, False) for i in range(10)]

jump_images = [pygame.image.load(f'images/mage/jump/({i}).png') for i in range(1, 11)]


class Mage:
    __IDLE_SPEED = 0.16

    def __init__(self):
        self.index = 0

    def idle_animation(self,direction):
        self.index += self.__IDLE_SPEED
        if direction == 'right':
            return idle_images_right[int(self.index) % len(idle_images_right)]
        return idle_images_left[int(self.index) % len(idle_images_left)]

    def walk_images(self, direction):
        self.index += self.__IDLE_SPEED
        if direction == "right":
            return walk_images_right[int(self.index) % len(walk_images_right)]
        return walk_images_left[int(self.index) % len(walk_images_left)]

    def jump_animation(self):
        self.index += self.__IDLE_SPEED
        return walk_images_right[int(self.index) % len(walk_images_right)]

    def attack_animation(self, direction):
        self.index += 0.1
        if direction == "right":
            return attack_images_right[int(self.index) % len(attack_images_right)]
        return attack_images_left[int(self.index) % len(attack_images_left)]
