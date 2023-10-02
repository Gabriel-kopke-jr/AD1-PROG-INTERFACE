from classes.mapa import Mapa
from utils import LEGENDA


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
        self._vision = vision[:len(vision)-1]
        print(vision)

    def is_valide_point(self,value):
        if not value.isdigit():
            print("A coordenada deve ser um número inteiro")
            return False
        return True
    def process_entry(self,x,y):
        vision = self.get_vision()
        bombs = self.get_bombs()
        test_tuple = (int(x),int(y))
        if test_tuple in bombs:
            self.set_is_not_end(False)
            self.generate_vision_end_game()
        else:
            self.generate_vision(x,y)
        self.check_is_end()
        return vision



    def generate_vision(self,x,y):
        vision = self.get_vision()
        vision = vision.split('\n')
        vision = [element.replace(' ', '') for element in vision]
        x_int, y_int = int(x), int(y)
        line = vision[x_int]
        new_line = self.generate_line_with_point_choiced(line,y_int)
        vision[x_int] = new_line
        self.update_vision(vision,x_int,y_int)
        print(self._vision)


    def update_vision(self,vision,x_int,y_int):

        result = ""
        for i in range(len(vision)):
            if i != 0:
                result += '\n'
            for j in range(len(vision)):
                result += vision[i][j]
        final_vision = self.fill_bombs(vision,x_int,y_int)
        self.set_vision(final_vision)

    def fill_bombs(self,vision,x_int,y_int):
        x_busca_sup, x_busca_inf = x_int - 1, x_int + 1
        y_busca_esq, y_busca_dir = y_int -1 , y_int + 1
        points_x = [x_busca_sup,x_busca_inf]
        points_y = [y_busca_esq,y_busca_dir]
        points_validated_x = [ Jogo.validate_point_negative(Jogo.validate_point_after_limit(element,len(vision),x_int),x_int) for element in points_x ]
        points_validated_y = [ Jogo.validate_point_negative(Jogo.validate_point_after_limit(element,len(vision),y_int),y_int) for element in points_y ]
        points_search = [(x, y) for x in points_validated_x for y in points_validated_y]
        vision_bombs = self.search_bombs(points_search,vision)
        return vision_bombs


    def search_bombs(self,points_search_bombs,vision):
        result = ""
        bombs = self.get_bombs()
        number = len([element for element in points_search_bombs if element in self.get_bombs()])
        for i in range(len(vision)):
            if i != 0:
                result += '\n'
            for j in range(len(vision)):
                if (i,j) in points_search_bombs:
                    result += f'{number}'
                else:
                    result += vision[i][j]
        return result




    @staticmethod
    def validate_point_negative(coordinate,limit):
        if coordinate < 0:
            return limit
        return coordinate

    @staticmethod
    def validate_point_after_limit(coordinate,tamanho_lista,limit):
        if coordinate > tamanho_lista:
            return limit
        return coordinate


    def check_is_end(self):
        vision = self.get_vision()
        vision = vision.split('\n')
        vision = [element.replace(' ', '') for element in vision]
        vision_to_check = []
        for line in vision:
            vision_to_check.extend(line)
        number_of_spaces = vision_to_check.count('_')
        if number_of_spaces <= 1:
            self.set_is_not_end(False)
            self.make_winner_vision()




    def make_winner_vision(self):
        vision = self.get_vision()
        result = ""
        for i in range(len(vision)):
            if i != 0:
                result += '\n'
            for j in range(len(vision)):
                if vision[i][j] == "_":
                    result += 'X'
                result += vision[i][j]
        self.set_vision(result)







    def get_vision(self):
        return self._vision

    def set_vision(self,vision):
        self._vision = vision

    def generate_line_with_point_choiced(self,line,y):
        new_line = ""
        for i in range(len(line)):
            if(i == y):
                new_line += 'X'
                continue
            new_line += line[i]
        return new_line

    def get_bombs(self):
        return self._mapa._bombs


    def generate_vision_end_game(self):
        vision = self.get_vision()
        vision = vision.split('\n')
        vision = [element.replace(' ','') for element in vision]
        bombs = self.get_bombs()
        result = ""
        for i in range(len(vision)):
            if i != 0:
                result += '\n'

            for j in range(len(vision)):
                if (i,j) in bombs:
                    result += "O "
                else:
                    result += 'X '
        print('Você pisou em uma bomba')
        print(LEGENDA)
        print(result)
        print("Fim de Jogo")





