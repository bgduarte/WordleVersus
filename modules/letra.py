

class Letra:

    # TODO: 
    def __init__(self, cor: str, letra: str):
        self.__cor = cor
        self.__letra = letra

    # TODO: 
    def caracter_valido(self, tecla_pressionada: str) -> bool:
        pass

    # TODO:     
    def preencher(self, letra: str) -> None:
        pass

    # TODO: 
    def apagar(self) -> None:
        pass

    def obterLetra(self) -> str:
        return self.__letra

    def obterCor(self) -> str:
        return self.__cor
