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

    def show_current_map(self):
        return self.maps[self.current_map].get_current_image()
