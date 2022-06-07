from jogador import Jogador

class Palavra:

    # TODO
    def __init__(self, letras: list, jogador: Jogador, letraAtual: int) -> None:
        self.__letras = letras
        self.__jogador = jogador
        self.__letraAtual = letraAtual

    # TODO
    def preencher_letra_atual(self, tecla_pressionada: str) -> None:
        pass

    # TODO
    def palavra_cheia(self) -> bool:
        pass

    # TODO
    def palavra_vazia(self) -> bool:
        pass

    # TODO
    def incrementar_letra_atual(self) -> None:
        pass

    # TODO
    def decrementar_letra_atual(self) -> None:
        pass

    # TODO
    def obter_palavra_str(self) -> str:
        pass

    # TODO
    def avaliar_palavra(palavra_secreta: str, jogador_que_tentou: Jogador) -> None:
        pass

    def definir_jogador(self, jogador: Jogador) -> None:
        self.__jogador = jogador