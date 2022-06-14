from modules.jogador import Jogador
from modules.letra import Letra

class Palavra:  
    def __init__(self, jogador) -> None:
        self.__letras = []
        for i in range(5):
            self.__letras.append(Letra())
        self.__jogador = jogador
        self.__letraAtual = 0


    def preencher_letra_atual(self, tecla_pressionada: str) -> None:
        if Letra.caracter_valido(tecla_pressionada):
            if tecla_pressionada == "\b":
                if not self.palavra_vazia():
                    self.__letras[self.__letraAtual-1].apagar()
                    self.__letraAtual -= 1
            else:
                if not self.palavra_cheia():
                    self.__letras[self.__letraAtual].preencher(tecla_pressionada)
                    self.__letraAtual += 1


    
    def palavra_cheia(self) -> bool:
        return self.__letraAtual == 5

    
    def palavra_vazia(self) -> bool:
        return self.__letraAtual == 0


    def obter_palavra_str(self) -> str:
        palavraStr = ""
        for letra in self.__letras:
            palavraStr += letra.obter_letra()
        return palavraStr


    def obter_letras(self) -> list:
        return self.__letras

    
    def avaliar_palavra(self, palavra_secreta: str, jogador_que_tentou: Jogador) -> None:
        print (f'Avaliando palavra:{self.obter_palavra_str()} com a palavra secreta:{palavra_secreta}')
        self.__jogador = jogador_que_tentou
        acertouPalavra = True
        for i in range (len(self.__letras)):
            letra = self.__letras[i].obter_letra()
            if letra in palavra_secreta:
                if letra == palavra_secreta[i]:
                    self.__letras[i].definir_cor("verde")
                else:
                    self.__letras[i].definir_cor("amarelo")
                    acertouPalavra = False
            else:
                self.__letras[i].definir_cor("cinza")
                acertouPalavra = False

        
        if acertouPalavra:
            self.__jogador.definir_como_vencedor()


    def definir_jogador(self, jogador: Jogador) -> None:
        self.__jogador = jogador

    def obter_jogador(self) -> Jogador:
        return self.__jogador