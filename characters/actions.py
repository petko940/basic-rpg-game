import pygame


class Actions:
    def __init__(self, x=-30, y=300):
        self.x = x
        self.y = y

    def idle(self):
        return self.x, self.y + 10

    def walk(self):
        if pygame.key.get_pressed()[pygame.K_d]:
            self.x += 1
        elif pygame.key.get_pressed()[pygame.K_a]:
            self.x -= 1
        else:
            self.x = self.x

        return self.x, self.y

    def attack(self):
        y = self.y - 100
        return self.x, y

    def check_for_traverse(self):
        if self.x >= 1750:
            self.x = -30
            return True
