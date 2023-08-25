from classes.mapa import Mapa


class Jogo:

    def __init__(self,dificult = 3):
        self._dificult = dificult


    def generate_map(self,dificult):
        mapa = Mapa()
        mapa.set_dificult(dificult)
        mapa.generate_pontos()
