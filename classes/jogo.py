from classes.mapa import Mapa


class Jogo:

    def __init__(self,dificult = 3):
        self._dificult = dificult
        self._is_not_end = True



    def generate_map(self):

        difficult = self.get_difficult()
        mapa = Mapa()
        mapa.set_dificult(difficult)
        mapa.generate_pontos()
        self._mapa = mapa

    def set_is_not_end(self,value):
        self._is_not_end = value

    def get_is_not_end(self):
        return self._is_not_end

    def get_difficult(self):
        return self._dificult

    def get_mapa_tamanho(self):
        return self._mapa.get_tamanho()

    def generate_first_vision(self):
        tamanho = self.get_mapa_tamanho()
        vision = ""
        line = ""
        for i in range(tamanho):
            line += " _"
        for i in range(tamanho):
            vision += line + '\n'
        print(vision)

    def validate_point(self,value):
        should_read_again = False
        if not value.isdigit():
            print("A coordenada x deve ser um número inteiro")
            should_read_again = True

        return should_read_again


