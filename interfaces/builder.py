from abc import ABC,abstractmethod


class Builder(ABC):

    @abstractmethod
    def build_map(self)->None:
        pass

    @abstractmethod
    def build_game(self)-> None:
        pass
