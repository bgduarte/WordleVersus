from modules.jogador import Jogador
from modules.consultorDicionario import ConsultorDicionario
from modules.palavra import Palavra
from modules.interfaceJogador import InterfaceJogador


class Partida:
    __jogador1: Jogador = None
    __jogador2: Jogador = None
    __palavraSecreta: str = None
    __tentativas: list = []
    __emAndamento: bool = False
    interface = None


    def iniciar_partida() -> None:
        Partida.__tentativas = [Palavra()]

        Partida.__jogador1 = Jogador(cor="azul", eh_seu_turno=True)
        Partida.__jogador2 = Jogador(cor="vermelho", eh_seu_turno=False)

        # TODO 
        Partida.__palavraSecreta = "WRITE" # ConsultorDicionario.pegar_palavra_aleatoria().upper()

        Partida.interface = InterfaceJogador(Partida)
        Partida.interface.atualizar_interface()
        Partida.__emAndamento = True # Arrumar no diagrama?


    def preencher_letras(tecla_pressionada: str) -> None:
        if Partida.__emAndamento:
            Partida.__tentativas[-1].preencher_letra_atual(tecla_pressionada)
            Partida.interface.atualizar_interface()


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


    def efetuar_troca_de_turno() -> None:
        print ("Efetuando troca de turno")
        Partida.__jogador1.passar_turno()
        Partida.__jogador2.passar_turno()
        Partida.interface.atualizar_interface()



    def realizar_tentativa() -> None:
        if Partida.__emAndamento:
            if Partida.verificar_validade_de_palavra():
                Partida.__tentativas[-1].avaliar_palavra(Partida.__palavraSecreta, Partida.jogador_da_vez())
                Partida.avaliar_encerramento_de_partida()
                if Partida.__emAndamento:
                    Partida.efetuar_troca_de_turno()
                else:
                    Partida.interface.atualizar_interface()


    def verificar_validade_de_palavra() -> bool:
        if Partida.__tentativas[-1].palavra_cheia():
            palavraStr = Partida.__tentativas[-1].obter_palavra_str()
            if (ConsultorDicionario.palavra_existe(palavraStr.lower())):
                return True

        return False

    
    def avaliar_encerramento_de_partida() -> None:
        print ('Jogador 1 eh vencedor: ' + str(Partida.__jogador1.obter_eh_vencedor()))
        print ('Jogador 2 eh vencedor: ' + str(Partida.__jogador2.obter_eh_vencedor()))
        if (Partida.__jogador1.obter_eh_vencedor() or Partida.__jogador2.obter_eh_vencedor()):
            Partida.__emAndamento = False
        else:
            if (len(Partida.__tentativas) == 6):
                Partida.__emAndamento = False
            else:
                Partida.__tentativas.append(Palavra())


    def obter_tentativas() -> list:
        return Partida.__tentativas
        