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
    x = input("Digite a coordenada x ")
    y = input("Digite a coordenada y ")
    should_read_again  = jogo.validate_points(x,y)
    if should_read_again:
        print("Digite novamente os pontos")
        continue


