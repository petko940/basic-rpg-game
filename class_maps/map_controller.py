from class_maps.all_maps.big_tree_forest import BigTreeForest
from class_maps.all_maps.bridge import Bridge
from class_maps.all_maps.forest import Forest
from class_maps.all_maps.green_big_forest import GreenBigForest
from class_maps.all_maps.narrow_forest import NarrowForest
from pygame import transform


class MapController:

    def __init__(self, arrows):
        self.maps = []
        self.current_map_index = 0

        self.arrow = [transform.rotate(arrows[i], 90) for i in range(len(arrows))]
        self.arrow_index = 0

    @property
    def leading_arrow_speed(self):
        return 0.25

    @property
    def __valid_maps(self):
        return {"Forest": Forest, "NarrowForest": NarrowForest, "BigTreeForest": BigTreeForest, "Bridge": Bridge,
                "GreenBigForest": GreenBigForest}

    @property
    def current_map(self):
        return self.maps[self.current_map_index]

    def create_map(self, images: list, map_name: str):
        if map_name in self.__valid_maps:
            new_map = self.__valid_maps[map_name](map_name, images)
            self.maps.append(new_map)

    def show_current_map(self):
        return self.current_map.get_current_image()

    def change_map_right_side(self):
        if self.current_map_index + 1 < len(self.maps):
            self.current_map_index += 1

    def change_map_left_side(self):
        if self.current_map_index - 1 >= 0:
            self.current_map_index -= 1

    def check_if_on_last_map(self):
        return self.maps[-1].get_image_index() == len(self.maps[-1].images) - 1

    def first_map_go_outside_left_side(self):
        return self.maps[0].first_image()

    def check_for_traverse(self, hero: object, monster):
        if hero.x >= self.current_map.MAP_WIDTH - 150:
            if monster.monsters_on_screen or self.check_if_on_last_map():
                hero.x = self.current_map.MAP_WIDTH - 150
                return

            if self.current_map.last_image():
                self.change_map_right_side()
                hero.x = -30
                return

            self.current_map.next_image()
            hero.x = -30

        elif hero.x <= -100:
            if monster.monsters_on_screen or self.first_map_go_outside_left_side():
                hero.x = -100
                return

            if self.current_map.first_image():
                self.change_map_left_side()
                hero.x = self.current_map.MAP_WIDTH - 200
                return

            self.current_map.previous_image()
            hero.x = self.current_map.MAP_WIDTH - 200

    def display_leading_arrow_on_cleared_stage(self, screen):
        stage = self.current_map

        if self.maps[-1].last_image():
            return

        if stage.check_stage_cleared():
            show_img = self.arrow[int(self.arrow_index) % len(self.arrow)]
            screen.blit(show_img, (1250, 100))

            self.arrow_index += self.leading_arrow_speed

    def spawn_monster_on_non_cleared_stage(self, monster):
        stage = self.current_map

        if not stage.check_stage_cleared():
            monster.increase_monsters_on_screen()

        # stage can't be cleared if the monster is alive
        if not monster.is_dead:
            return

        stage.clear_stage()
