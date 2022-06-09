

class Letra:

    
    def __init__(self):
        self.__cor = "branca"
        self.__letra = " "

    # TODO: 
    def caracter_valido(tecla_pressionada: str) -> bool:
        return True

 
    def preencher(self, letra: str) -> None:
        self.__letra = letra.upper()


    def apagar(self) -> None:
        self.__letra = " "


    def obter_letra(self) -> str:
        return self.__letra


    def obter_cor(self) -> str:
        return self.__cor

    def definir_cor(self, cor: str) -> None:
        self.__cor = cor
