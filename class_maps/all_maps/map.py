from abc import ABC


class Map(ABC):
    MAP_WIDTH = 1366

    def __init__(self, name: str, images: list):
        self.name = name
        self.images = images
        self.index = 0
        self.cleared_stages = {stage: False for stage in range(len(self.images))}

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        if not 0 <= value < len(self.images):
            raise Exception(f"{value} index of the image must be in the list range")
        self.__index = value

    def check_stage_cleared(self):
        return self.cleared_stages[self.index]

    def clear_stage(self):
        self.cleared_stages[self.index] = True

    def get_current_image(self):
        return self.images[self.index]

    def next_image(self):
        if self.index + 1 < len(self.images):
            self.index += 1

    def previous_image(self):
        if self.index - 1 >= 0:
            self.index -= 1

    def get_image_index(self):
        return self.index

    def last_image(self):
        return self.index == len(self.images) - 1

    def first_image(self):
        return self.index == 0

    def get_map_width(self):
        return self.MAP_WIDTH
