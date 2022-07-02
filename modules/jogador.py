class Jogador:
    
    def __init__(self, cor: str, eh_seu_turno: bool) -> None:
        self.__cor = cor
        self.__eh_vencedor = False
        self.__eh_seu_turno = eh_seu_turno
        self.__podePassarTurno = True

    
    def tentar_passar_turno(self) -> bool:
        if self.__podePassarTurno:
            self.__podePassarTurno = False
            return True
        return False

    
    def passar_turno(self) -> None:
        self.__eh_seu_turno = not self.__eh_seu_turno


    def definir_como_vencedor(self) -> None:
        self.__eh_vencedor = True


    def obter_eh_vencedor(self) -> bool:
        return self.__eh_vencedor


    def obter_eh_seu_turno(self) -> bool:
        return self.__eh_seu_turno


    def obter_cor(self) -> str:
        return self.__cor

    def pode_passar_turno(self) -> bool:
        return self.__podePassarTurno
    
