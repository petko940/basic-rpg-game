class Mage:
    __IDLE_SPEED = 0.16

    def __init__(self):
        self.index = 1

    def idle_animation(self):
        self.index += self.__IDLE_SPEED
        return idle_images[int(self.index) % len(idle_images)]

    def jump_animation(self):
        self.index += 0.1
        return jump_images[int(self.index) % len(jump_images)]
