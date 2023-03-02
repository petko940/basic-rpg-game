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

            print(f"map {map_name} with length of {len(images)} images was added")

    def get_current_map(self):
        return self.maps[self.current_map]

    def show_current_map(self):
        return self.maps[self.current_map].get_current_image()

    def check_for_traverse(self, hero: object):
        if hero.x >= self.get_current_map().MAP_WIDTH - 150:
            if self.maps[self.current_map].get_image_index() == len(self.maps[self.current_map].images) - 1:
                hero.x = self.get_current_map().MAP_WIDTH - 150

            else:
                self.maps[self.current_map].next_image()
                hero.x = -30

        elif hero.x <= -100:
            if self.maps[self.current_map].get_image_index() == 0:
                hero.x = -100

            else:
                self.maps[self.current_map].previous_image()
                hero.x = self.get_current_map().MAP_WIDTH - 200
