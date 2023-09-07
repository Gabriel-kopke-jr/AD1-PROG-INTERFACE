from classes.jogo import Jogo
from utils import MENU,JOGO_CAMPO_MINADO
print(JOGO_CAMPO_MINADO)
print(MENU)

dificuldade = input()

dificuldade = int(dificuldade)

jogo = Jogo(dificuldade)

jogo.generate_map()


jogo.generate_first_vision()

while jogo.get_is_not_end():
    should_read_again = False
    while should_read_again == False:
        x = input("Digite a coordenada x ")
        is_valid_x = jogo.is_valide_point(x)
        y = input("Digite a coordenada y ")
        is_valid_y = jogo.is_valide_point(y)
        should_read_again = is_valid_x and is_valid_y
    jogo.process_entry(x,y)





