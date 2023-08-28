from random import randint
from math import ceil
class Mapa:


    def generate_pontos(self):
        tamanho = self.get_tamanho()
        pontos = [(i,j) for i in range(tamanho) for j in range(tamanho)]
        self.allocate_bombs_and_points(pontos)


    def get_tamanho(self):
        return self._tamanho

    def set_tamanho(self):
        difficult = self.get_dificult()
        self._tamanho = TAMANHO_DIFFICULT_MAPPER[difficult]

    def allocate_bombs_and_points(self,pontos):
        pontos_copy = pontos.copy()
        tamanho = self.get_tamanho()
        bombs = []
        while self.bombs_is_not_allocated(bombs):
            x = randint(0,tamanho-1)
            y = randint(0,tamanho-1)

            if (x,y) not in bombs:
                bombs.append((x,y))
                pontos_copy.remove((x,y))

        self._bombs = bombs
        self._pontos =pontos_copy


    def set_dificult(self,dificult):
        self._dificult = dificult
        self.set_tamanho()
        self.set_bomb_rate()

    def get_dificult(self):
        return self._dificult

    def set_bomb_rate(self):
        dificult = self.get_dificult()
        self._bomb_rate = DIFICULT_MAPPER_BOMB_RATE[dificult]

    def get_boomb_rate(self):
        return self._bomb_rate


    def bombs_is_not_allocated(self,bombs):
        tamanho = self.get_tamanho()
        total_pontos = tamanho**2
        bombas = total_pontos*self.get_boomb_rate()
        return len(bombs) < ceil(bombas)



DIFICULT_MAPPER_BOMB_RATE = {
        1: 0.2,
        2: 0.3,
        3: 0.4,
        4: 0.5,
        5: 0.6
}

TAMANHO_DIFFICULT_MAPPER = {
    1: 3,
    2: 4,
    3: 5,
    4: 6,
    5: 7
}