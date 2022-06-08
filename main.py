from modules.partida import Partida
from modules.consultorDicionario import ConsultorDicionario
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

Partida.iniciar_partida()
Partida.preencher_letras("p")
Partida.preencher_letras("r")
Partida.preencher_letras("i")
Partida.preencher_letras("n")
Partida.preencher_letras("t")
Partida.realizar_tentativa()

Partida.preencher_letras("p")
Partida.preencher_letras("r")
Partida.preencher_letras("i")
Partida.preencher_letras("n")
Partida.preencher_letras("t")
Partida.realizar_tentativa()

Partida.preencher_letras("w")
Partida.preencher_letras("o")
Partida.preencher_letras("l")
Partida.preencher_letras("v")
Partida.preencher_letras("e")
Partida.realizar_tentativa()

Partida.passar_turno()
Partida.passar_turno()
Partida.passar_turno()

Partida.preencher_letras("w")
Partida.preencher_letras("r")
Partida.preencher_letras("i")
Partida.preencher_letras("t")
Partida.preencher_letras("e")
Partida.realizar_tentativa()

