from random import randint
from math import floor
class Mapa:


    def generate_pontos(self):
        tamanho = self.get_tamanho()
        pontos = [(i,j) for i in range(tamanho) for j in range(tamanho)]
        self.allocate_bombs_and_points(pontos)


    def get_tamanho(self):
        return self._tamanho

    def set_tamanho(self,tamanho):
        self._tamanho = tamanho

    def allocate_bombs_and_points(self,pontos):
        pontos_copy = pontos.copy()
        tamanho = self.get_tamanho()
        bombs = []
        while self.bombs_is_not_allocated(bombs):
            x = randint(0,tamanho)
            y = randint(0,tamanho)

            if (x,y) not in bombs:
                bombs.append((x,y))
                pontos_copy.remove((x,y))

        self._bombs = bombs
        self._pontos =pontos


    def set_dificult(self,dificult):
        self._dificult = dificult

    def get_dificult(self):
        return self._dificult

    def set_bomb_rate(self):
        dificult = self.get_dificult()
        self._bomb_rate = DIFICULT_MAPPER[dificult]

    def get_boomb_rate(self):
        return self._bomb_rate


    def bombs_is_not_allocated(self,bombs):
        tamanho = self.get_tamanho()
        total_pontos = tamanho**2
        bombas = total_pontos*self.get_boomb_rate()
        return len(bombs) == floor(bombas)



DIFICULT_MAPPER = {
        1: 0.2,
        2: 0.3,
        3: 0.4,
        4: 0.5,
        5: 0.6
}