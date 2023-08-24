from classes.jogo import Jogo
from interfaces.builder import Builder


class ConcreteBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._jogo = Jogo()