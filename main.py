from modules.interfaceJogador import InterfaceJogador
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

InterfaceJogador()