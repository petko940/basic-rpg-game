import pygame

idle_images = [pygame.image.load(f'images/mage/idle/({i}).png') for i in range(1, 11)]
attack_images = [pygame.image.load(f'images/mage/attack/({i}).png') for i in range(1, 11)]
die_images = [pygame.image.load(f'images/mage/die/({i}).png') for i in range(1, 11)]
walk_images_right = [pygame.image.load(f'images/mage/walk/({i}).png') for i in range(1, 11)]
jump_images = [pygame.image.load(f'images/mage/jump/({i}).png') for i in range(1, 11)]


class Mage:
    __IDLE_SPEED = 0.16

    def __init__(self):
        self.index = 0
        self.is_selected = False

    def idle_animation(self):
        self.index += self.__IDLE_SPEED
        return idle_images[int(self.index) % len(idle_images)]

    def jump_animation(self):
        self.index += 0.1
        return jump_images[int(self.index) % len(jump_images)]