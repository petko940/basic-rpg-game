from characters.hero import Hero


class Mage(Hero):

    def __init__(self, x: int, y: int, attack_images: list, die_images: list, idle_images: list, jump_images: list,
                 walk_images: list):
        super().__init__(x, y, attack_images, die_images, idle_images, jump_images, walk_images)


