class Jogador:

    # TODO
    def __init__(self, cor: str, ehVencedor: bool, ehSeuTurno: bool, podePassarTurno: bool) -> None:
        self._cor = cor
        self._ehVencedor = ehVencedor
        self._ehSeuTurno = ehSeuTurno
        self._podePassarTurno = podePassarTurno

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
        return self._ehVencedor
    
