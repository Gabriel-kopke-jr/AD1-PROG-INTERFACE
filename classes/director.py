from classes.concrete_builder import ConcreteBuilder


class Director:

    def __init__(self) -> None:
        self._builder = None


    @property
    def builder(self) -> ConcreteBuilder:
        return self._builder


    def builder_game(self) -> None:
        self.builder.generate_map()
        self.builder.generate_game()
