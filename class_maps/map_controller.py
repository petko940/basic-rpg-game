from class_maps.all_maps.forest import Forest


class MapController:

    def __init__(self):
        self.maps = []
        self.current_map = 0

    @property
    def __valid_maps(self):
        return {"Forest": Forest}

    def create_map(self, images: list, map_name: str):
        if map_name in self.__valid_maps:
            new_map = self.__valid_maps[map_name](map_name, images)
            self.maps.append(new_map)

    def get_current_map(self):
        return self.maps[self.current_map]

    def show_current_map(self):
        return self.maps[self.current_map].get_current_image()

    def check_if_on_last_map(self):
        return self.maps[self.current_map].get_image_index() == len(self.maps[self.current_map].images) - 1

    def first_map_go_outside_left_side(self):
        return self.maps[self.current_map].get_image_index() == 0

    def check_for_traverse(self, hero: object, monster):
        if hero.x >= self.get_current_map().MAP_WIDTH - 150:
            if monster.monsters_on_screen or self.check_if_on_last_map():
                hero.x = self.get_current_map().MAP_WIDTH - 150

            else:
                self.maps[self.current_map].next_image()
                hero.x = -30

        elif hero.x <= -100:
            if monster.monsters_on_screen or self.first_map_go_outside_left_side():
                hero.x = -100

            else:
                self.maps[self.current_map].previous_image()
                hero.x = self.get_current_map().MAP_WIDTH - 200
