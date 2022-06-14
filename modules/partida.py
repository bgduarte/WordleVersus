from turtle import Terminator
from modules.jogador import Jogador
from modules.consultorDicionario import ConsultorDicionario
from modules.palavra import Palavra


class Partida:
    def __init__(self) -> None:
        self.__jogador1: Jogador = None
        self.__jogador2: Jogador = None
        self.__palavraSecreta: str = None
        self.__tentativas: list = []
        self.__emAndamento: bool = False

    def iniciar_partida(self) -> None:
        self.__jogador1 = Jogador(cor="azul", eh_seu_turno=True)
        self.__jogador2 = Jogador(cor="vermelho", eh_seu_turno=False)

        self.__tentativas = [Palavra(self.__jogador1)]

        self.__palavraSecreta = ConsultorDicionario.pegar_palavra_aleatoria().upper()

        self.__emAndamento = True # Arrumar no diagrama?


    def preencher_letras(self, tecla_pressionada: str) -> None:
        if self.__emAndamento:
            self.__tentativas[-1].preencher_letra_atual(tecla_pressionada)


    def passar_turno(self) -> None:
        if self.__emAndamento:
            jogador_da_vez = self.jogador_da_vez()
            if jogador_da_vez.tentar_passar_turno():
                self.efetuar_troca_de_turno()
    

    def jogador_da_vez(self) -> Jogador:
        if self.__jogador1.obter_eh_seu_turno():
            return self.__jogador1
        else:
            return self.__jogador2


    def efetuar_troca_de_turno(self) -> None:
        self.__jogador1.passar_turno()
        self.__jogador2.passar_turno()
        self.__tentativas[-1].definir_jogador(self.jogador_da_vez())


    def realizar_tentativa(self) -> None:
        if self.__emAndamento:
            if self.verificar_validade_de_palavra():
                self.__tentativas[-1].avaliar_palavra(self.__palavraSecreta, self.jogador_da_vez())
                self.avaliar_encerramento_de_partida()
                if self.__emAndamento:
                    self.efetuar_troca_de_turno()


    def verificar_validade_de_palavra(self) -> bool:
        if self.__tentativas[-1].palavra_cheia():
            palavraStr = self.__tentativas[-1].obter_palavra_str()
            if (ConsultorDicionario.palavra_existe(palavraStr.lower())):
                return True

        return False

    
    def avaliar_encerramento_de_partida(self) -> None:
        if (self.__jogador1.obter_eh_vencedor() or self.__jogador2.obter_eh_vencedor()):
            self.__emAndamento = False
        else:
            if (len(self.__tentativas) == 6):
                self.__emAndamento = False
            else:
                self.__tentativas.append(Palavra(self.jogador_da_vez()))


    def obter_tentativas(self) -> list:
        return self.__tentativas
    
    def obter_palavra_secreta(self) -> str:
        return self.__palavraSecreta

    def obter_em_andamento(self) -> bool:
        return self.__emAndamento

    def obter_vencedor(self):
        if self.__jogador1.obter_eh_vencedor():
            return self.__jogador1
        elif self.__jogador2.obter_eh_vencedor():
            return self.__jogador2
        else:
            None

        