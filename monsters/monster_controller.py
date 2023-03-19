from pygame import draw
from monsters.monster import Monster


class MonsterController:

    def __init__(self, *monsters: Monster):
        self.monsters = [*monsters]
        self.first_spawn = False

    @property
    def current_monster(self):
        return self.monsters[0]

    def display_health_bar(self, screen):
        if not self.current_monster.is_dead:
            draw.rect(screen, self.current_monster.HEALTH_BAR_PAD_COLOR, self.current_monster.health_bar_pad_position())
            draw.rect(screen, self.current_monster.HEALTH_BAR_COLOR, self.current_monster.health_bar_position())

    def lower_attack_cooldown(self, amount):
        monster = self.current_monster

        if monster.attack_cooldown:
            monster.attack_cooldown -= amount

            if monster.attack_cooldown <= 0:
                monster.attack_cooldown = 0

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

        if not self.current_monster.check_target_reached(player.x):
            image = monster.walk(player.x)
            screen.blit(image, monster.monster_position())

    def stay_idle(self, screen, player):
        monster = self.current_monster

        if not self.current_monster.check_target_reached(player.x):
            return

        if not monster.is_attacking and not monster.is_dead:
            image = monster.idle()
            screen.blit(image, monster.monster_position())

    def attack_target(self, screen, player):
        monster = self.current_monster

        if not monster.is_attacking:

            if monster.attack_cooldown or monster.is_dead:
                return

            if not self.current_monster.check_target_reached(player.x):
                return

        monster.attack()

        if monster.check_valid_index(monster.non_looped_index, monster.attack_left):
            index_and_animation = int(monster.non_looped_index), monster.attack_left, monster.attack_right
            screen.blit(monster.get_image(*index_and_animation), monster.monster_position())

            monster.increase_index_attack_animation()

        monster.check_end_of_attack()

        if monster.attack_cooldown:
            player.take_damage(monster.damage)

    def die(self, screen, player):
        monster = self.current_monster
        if not monster.is_dead:
            return

        if not monster.check_valid_index(int(monster.non_looped_index), monster.die_left):
            monster.set_default_values_after_death()
            monster.remove_monster_from_screen()
            player.gain_experience(monster.experience_reward)
            return

        image = monster.death()
        screen.blit(image, monster.monster_position())

        monster.increase_death_image_index()

    def actions(self, screen, player):
        if not self.current_monster.monsters_on_screen:
            return
        self.chase_player(screen, player)

        self.stay_idle(screen, player)

        self.attack_target(screen, player)

        self.die(screen, player)
