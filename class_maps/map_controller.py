from class_maps.all_maps.forest import Forest


class MapController:

    def __init__(self):
        self.maps = []
        self.current_map_index = 0

    @property
    def __valid_maps(self):
        return {"Forest": Forest}

    @property
    def current_map(self):
        return self.maps[self.current_map_index]

    def create_map(self, images: list, map_name: str):
        if map_name in self.__valid_maps:
            new_map = self.__valid_maps[map_name](map_name, images)
            self.maps.append(new_map)

    def show_current_map(self):
        return self.current_map.get_current_image()

    def check_if_on_last_map(self):
        return self.maps[-1].get_image_index() == len(self.current_map.images) - 1

    def first_map_go_outside_left_side(self):
        return self.current_map.get_image_index() == 0

    def check_for_traverse(self, hero: object, monster):
        if hero.x >= self.current_map.MAP_WIDTH - 150:
            if monster.monsters_on_screen or self.check_if_on_last_map():
                hero.x = self.current_map.MAP_WIDTH - 150

            else:
                self.current_map.next_image()
                hero.x = -30

        elif hero.x <= -100:
            if monster.monsters_on_screen or self.first_map_go_outside_left_side():
                hero.x = -100

            else:
                self.current_map.previous_image()
                hero.x = self.current_map.MAP_WIDTH - 200

    def spawn_monster_on_non_cleared_stage(self, monster):
        stage = self.current_map

        if stage.check_stage_cleared():
            return

        if not monster.is_dead:
            return

        stage.clear_stage()
        monster.power_up_after_death()

        if monster.can_spawn_monster():
            monster.increase_monsters_on_screen()

