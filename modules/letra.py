

class Letra:

    # TODO: 
    def __init__(self, cor: str, letra: str):
        self._cor = cor
        self._letra = letra

    # TODO: 
    def caracter_valido(self, teclaPressionada: str) -> bool:
        pass

    # TODO:     
    def preencher(self, letra: str) -> None:
        pass

    # TODO: 
    def apagar(self) -> None:
        pass

    def obterLetra(self) -> str:
        return self._letra

    def obterCor(self) -> str:
        return self._cor
