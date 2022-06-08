class InterfaceJogador:


    def __init__(self, partida):
        self.__partida = partida


    def atualizar_interface(self):
        print("--------------------------------------------------------------------------------")
        for tentativa in self.__partida.obter_tentativas():
            print ("{")
            if tentativa.obter_jogador():
                print ("Jogador: " + tentativa.obter_jogador().obter_cor())
            for letra in tentativa.obter_letras():
                print (letra.obter_letra(), end="")
            print ("")
            for letra in tentativa.obter_letras():
                print (letra.obter_cor() + ", ", end="")
            print ("")
            print ("}")
        print("--------------------------------------------------------------------------------")
        


    def realizar_tentiva(self):
        self.__partida.realizar_tentativa()


    def preencher_letras(self, teclaPressionada):
        self.__partida.preencher_letra(teclaPressionada)
        
    
    def passar_turno(self):
        self.__partida.passar_turno()