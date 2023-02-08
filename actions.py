import pygame


class Actions:
    def __init__(self, x=100, y=300):
        self.x = x
        self.y = y

    def walk(self):
        if pygame.key.get_pressed()[pygame.K_d]:
            self.x += 1
        else:
            self.x = self.x
        return self.x, self.y
