from typing import List
from pygame import draw, Rect
from monsters.monster import Monster


class MonsterController:

    def __init__(self, *monsters: Monster):
        self.monsters: List[Monster] = [*monsters]
        self.first_spawn = False

    @property
    def current_monster(self):
        return self.monsters[0]

    def display_health_bar(self, screen):
        if not self.current_monster.is_dead:
            draw.rect(screen, self.current_monster.HEALTH_BAR_PAD_COLOR, self.current_monster.health_bar_pad_position())
            draw.rect(screen, self.current_monster.HEALTH_BAR_COLOR, self.current_monster.health_bar_position())

    def spawn_monster(self):
        monster = self.current_monster

        if not self.first_spawn:
            self.first_spawn = True

        if monster.can_spawn_monster():
            monster.increase_monsters_on_screen()

    def chase_player(self, screen, player):
        monster = self.current_monster

        if monster.is_dead or monster.is_attacking:
            return

        image = monster.walk(player.x)
        screen.blit(image, monster.monster_position())

    def stay_idle(self, screen):
        monster = self.current_monster

        if not monster.is_attacking and not monster.is_dead:
            image = monster.idle()
            screen.blit(image, monster.monster_position())

    def actions(self, screen, player):
        draw.rect(screen, (255, 0, 0), self.current_monster.rect_hit_box, 3)

        if not self.current_monster.check_target_reached(player.x):
            self.chase_player(screen, player)
            return

        self.stay_idle(screen)
