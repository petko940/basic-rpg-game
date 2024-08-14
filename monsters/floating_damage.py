from utils import numbers_format, create_font


class FloatingDamage:

    def __init__(self,
                 damage: float,
                 target_x: float,
                 target_y: float,
                 heal=False):
        self.damage = f"{'-' if not heal else '+'}{numbers_format(num=damage)}"

        self.damage_surface = create_font(value=self.damage,
                                                  font="Georgia",
                                                  size_font=70,
                                                  colour=(255, 0, 0) if not heal else (0, 255, 0),
                                                  )

        self.damage_shadow = create_font(value=self.damage,
                                                 font="Georgia",
                                                 size_font=70,
                                                 colour=(0, 0, 0),
                                                 )

        self.damage_position = [target_x, target_y - 60]
        self.shadow_offset_position = [target_x + 3, target_y - 60 + 3]

        self.float_speed = 3
        self.remove_alpha = 6
        self.alpha = 255

    @property
    def is_faded(self):
        return self.alpha < 0

    def move_damage_up(self):
        self.damage_position[1] -= self.float_speed
        self.shadow_offset_position[1] -= self.float_speed

    def float(self):
        self.move_damage_up()
        self.alpha -= self.remove_alpha

        if self.is_faded:
            return

        self.damage_shadow.set_alpha(self.alpha)
        self.damage_surface.set_alpha(self.alpha)

    def display_damage(self, screen):
        screen.blit(self.damage_shadow, self.shadow_offset_position)
        screen.blit(self.damage_surface, self.damage_position)

    def render(self, screen):
        self.float()
        self.display_damage(screen)