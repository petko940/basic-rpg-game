from typing import List
import pygame
from monsters.monster import Monster


class MonsterController:

    def __init__(self, *monsters: Monster):
        self.monsters: List[Monster] = [*monsters]
        self.first_spawn = False

    @property
    def current_monster(self):
        return self.monsters[0]

    @property
    def target_reached(self):
        return self.current_monster.target_reached

    def spawn_monster(self):
        monster = self.current_monster

        if not self.first_spawn:
            self.first_spawn = True

        if monster.can_spawn_monster():
            monster.increase_monsters_on_screen()

    def chase_player(self, screen, player):
        monster = self.current_monster

        if self.target_reached or monster.is_dead or monster.is_attacking:
            return

        image = monster.walk(player.x)
        screen.blit(image, monster.monster_position())

    def stay_idle(self, screen):
        monster = self.current_monster

        if self.target_reached and not monster.is_attacking and not monster.is_dead:
            image = monster.idle()
            screen.blit(image, monster.monster_position())

    def actions(self, screen, player):
        self.chase_player(screen, player)
        self.stay_idle(screen)
