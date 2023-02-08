from class_maps.all_maps.map import Map


class Forest(Map):

    def __init__(self, name: str, images: list, index=0):
        super().__init__(name, images, index)
