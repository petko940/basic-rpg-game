from monsters.monster import Monster
from pygame import load, transform


class Demon(Monster):

    def __init__(self):
        super().__init__()

        self.attack_left = [load.image(f'monsters/demon_sprites/attack/{i}.png') for i in range(4)]
        self.attack_right = [transform.flip(self.attack_left[i], True, False) for i in range(len(self.attack_left))]

        self.die_left = [load.image(f'monsters/demon_sprites/death/{i}.png') for i in range(6)]
        self.die_right = [transform.flip(self.die_left[i], True, False) for i in range(len(self.die_left))]

        self.idle_left = [load.image(f'monsters/demon_sprites/idle/{i}.png') for i in range(3)]
        self.idle_right = [transform.flip(self.idle_left[i], True, False) for i in range(len(self.idle_left))]

        self.walk_left = [load.image(f'monsters/demon_sprites/walk/{i}.png') for i in range(6)]
        self.walk_right = [transform.flip(self.walk_left[i], True, False) for i in range(len(self.walk_left))]

    def idle(self):
        pass
