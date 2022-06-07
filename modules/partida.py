from xmlrpc.client import Boolean
from jogador import Jogador
from consultorDicionario import ConsultorDicionario
from palavra import Palavra

class Partida:
    # TODO
    # Atribbutes
    __jogador1: Jogador = None
    __jogador2: Jogador = None
    __palavraSecreta: str = None
    __tentativas: list = []
    __emAndamento: Boolean = False
    __interface = None

    # TODO
    def iniciar_partida() -> None:
        Partida.__tentativas = [Palavra()]

        Partida.__jogador1 = Jogador(cor="azul", ehSeuTurno=True)
        Partida.__jogador2 = Jogador(cor="vermelho", ehSeuTurno=False)

        Partida.__palavraSecreta = ConsultorDicionario.pegar_palavra_aleatoria()

        # TODO: Instanciar interface e chamar atualizar_interface()

    # TODO
    def preencher_letra(tecla_pressionada: str) -> None:
        if Partida.__emAndamento:
            Partida.__tentativas[-1].preencher_letra_atual(tecla_pressionada)
            # TODO atualizar_interface()


    def passar_turno() -> None:
        if Partida.__emAndamento:
            jogador_da_vez = Partida.jogador_da_vez()
            if jogador_da_vez.tentar_passar_turno():
                Partida.efetuar_troca_de_turno()
    

    def jogador_da_vez() -> Jogador:
        if Partida.__jogador1.obter_eh_seu_turno():
            return Partida.__jogador1
        else:
            return Partida.__jogador2

    # TODO
    def efetuar_troca_de_turno() -> None:
        Partida.__jogador1.passar_turno()
        Partida.__jogador2.passar_turno()
        # TODO: atualizar_interface()

    # TODO
    def realizar_tentativa() -> None:
        if Partida.__emAndamento:
            palavraValida = Partida.verificar_validade_de_palavra
            if palavraValida:
                Palavra.__tentativas[-1].avaliar_palavra(Partida.__palavraSecreta, Partida.jogador_da_vez())
                Palavra.avaliar_encerramento_de_partida()
                if Partida.__emAndamento:
                    Partida.efetuar_troca_de_turno()
                else:
                    pass
                    # TODO: atualizar_interface()


    def verificar_validade_de_palavra() -> Boolean:
        if Partida.__tentativas[-1].palavra_cheia():
            palavraStr = Partida.__tentativas[-1].obter_palavra_str()
            if (ConsultorDicionario.palavra_existe(palavraStr)):
                return True

        return False

    # TODO
    def avaliar_encerramento_de_partida() -> None:
        pass

    # TODO
    def obter_tentativas() -> list:
        pass
        