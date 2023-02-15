from characters.hero import Hero


class Hunter(Hero):

    def __init__(self, x: int, y: int, attack_images: list, die_images: list, idle_images: list, jump_images: list,
                 walk_images: list):
        super().__init__(x, y, attack_images, die_images, idle_images, jump_images, walk_images)

        self.mana_bar = self.make_bar(0, 35, self.BAR_LENGTH, 35)

        self.max_health = 100
        self.health = 100

        self.max_mana = 80
        self.mana = 80
