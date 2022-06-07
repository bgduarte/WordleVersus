class Jogador:

    # TODO
    def __init__(self, cor: str, ehVencedor: bool, ehSeuTurno: bool, podePassarTurno: bool) -> None:
        self.__cor = cor
        self.__ehVencedor = ehVencedor
        self.__ehSeuTurno = ehSeuTurno
        self.__podePassarTurno = podePassarTurno

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
        return self.__ehVencedor
    
