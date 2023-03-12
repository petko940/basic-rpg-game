from abc import ABC, abstractmethod


class Monster(ABC):

    def __init__(self):
        self.first_spawn = False

    @abstractmethod
    def idle(self):
        pass
