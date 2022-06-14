from modules.interfaceJogador import InterfaceJogador
import os

from modules.partida import Partida

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

partida  = Partida()
interface = InterfaceJogador(partida=partida)
interface.iniciar_partida()
