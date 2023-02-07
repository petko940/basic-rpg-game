from abc import ABC


class Map(ABC):

    def __init__(self, name: str, images: list, index=0):
        self.name = name
        self.images = images
        self.index = index

    def get_current_image(self):
        return self.images[self.index]

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        if not 0 <= value < len(self.images):
            raise Exception(f"{value} index of the image must be in the list range")
        self.__index = value
