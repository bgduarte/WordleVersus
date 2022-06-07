class Jogador:

    # TODO
    def __init__(self, cor: str, eh_seu_turno: bool) -> None:
        self.__cor = cor
        self.__eh_vencedor = False
        self.__eh_seu_turno = eh_seu_turno
        self.__podePassarTurno = True

    # TODO
    def tentar_passar_turno(self) -> bool:
        pass

    # TODO
    def passar_turno(self) -> None:
        pass

    # TODO
    def definir_como_vencedor(self) -> None:
        pass

    def obter_eh_vencedor(self) -> bool:
        return self.__eh_vencedor

    def obter_eh_seu_turno(self) -> bool:
        return self.__eh_seu_turno
    
