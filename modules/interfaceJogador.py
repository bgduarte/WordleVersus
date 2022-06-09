from tkinter import *
from modules.partida import Partida

# TODO: mudar o nome para ator jogador?
class InterfaceJogador:


    def __init__(self):
        self.janela_principal = Tk()
        self.janela_principal.title("Wordle Versus")
        self.janela_principal.geometry("900x900")
        self.janela_principal.resizable(False, False)
        self.janela_principal["bg"] = "gray"

        height, width = 1000, 1000

        self.frame_titulo = self.__criaFrame(self.janela_principal, height=0.75*height/10, width=width, bg='gray')
        self.frame_jogo = self.__criaFrame(self.janela_principal, height=6.25*height/10, width=width, bg='gray')
        self.frame_mensagens = self.__criaFrame(self.janela_principal, height=3*height/10, width=width, bg='gray')
        
        self.transparente = PhotoImage(file="images/transparente.png")
        cinza = PhotoImage(file="images/cinza.png")
        verde = PhotoImage(file="images/verde.png")
        amarelo = PhotoImage(file="images/amarelo.png")
        self.imagens = [cinza, verde, amarelo]
        
        
        self.__criaLabel(self.frame_titulo, 20, text='Wordle Versus', font=self.__fonte(25))
        
        self.letras = []
        self.frames_tentativas = []
        self.counter = 0
        for y in range(6):
            corJogador = 'grey'
            frames_tentativas = self.__criaFrame(self.frame_jogo, pady=3, height=(7*height/10)/6, width=6*width/10, bg=corJogador)
            for x in range(5):
                letra = Label(frames_tentativas, text=' ', font=self.__fonte(30), compound='center', relief='solid', image=self.transparente)
                letra.grid(row=0, column=x, padx=2, pady=8)
                self.frames_tentativas.append(frames_tentativas)
                self.letras.append(letra)

        self.frame_instrucoes = self.__criaFrame(self.frame_mensagens, height=3*(3*height/10)/10, width=width, bg='gray')
        self.frame_jogador = self.__criaFrame(self.frame_mensagens, height=2*(3*height/10)/10, width=width, bg='gray')
        self.frame_reset = self.__criaFrame(self.frame_mensagens, height=3*(3*height/10)/10, width=width, bg='gray')
        self.__criaLabel(self.frame_instrucoes, side='left', text="Pressione . para passar seu turno", font=self.__fonte(14))
        self.__criaLabel(self.frame_instrucoes, side='right', text="Pressione ENTER para submeter sua tentativa", font=self.__fonte(14))
        self.__criaLabel(self.frame_jogador, text='Jogador 1, é a sua vez!', font=self.__fonte(20))
        self.__criaLabel(self.frame_reset, text="Pressione CTRL para reiniciar o jogo", font=self.__fonte(14))
        
        self.janela_principal.bind('<Return>', lambda event: self.realizar_tentiva())
        self.janela_principal.bind('<Control_L>', lambda event: self.iniciar_partida())
        self.janela_principal.bind('.', lambda event: self.passar_turno(event))
        self.janela_principal.bind('<Key>', lambda event: self.preencher_letras(event))
        
        self.iniciar_partida()
        self.janela_principal.mainloop()

    
    def atualizar_interface(self):
        print("--------------------------------------------------------------------------------")
        for tentativa in Partida.obter_tentativas():
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
        

    def atualizar(self):
        self.atualizar_interface()
        print("Atualizando interface")
        tentativas = Partida.obter_tentativas()
        for j in range(len(self.frames_tentativas)):
            if len(tentativas) > j:
                letras = tentativas[j].obter_letras()
                for i in range(len(letras)):
                    if letras[i].obter_letra() != '':
                        self.letras[i+j*5].configure(text=letras[i].obter_letra() , 
                                                    image=self.pegarImagemDeCor(letras[i].obter_cor()),
                                                    font=self.__fonte(30), compound='center')
        


    def pegarImagemDeCor(self, cor):
        if cor == "verde":
            return self.imagens[1]
        elif cor == "amarelo":
            return self.imagens[2]
        elif cor == "cinza":
            return self.imagens[0]
        else:
            return self.transparente

    def iniciar_partida(self):
        Partida.iniciar_partida()
        self.atualizar()


    def realizar_tentiva(self):
        Partida.realizar_tentativa()
        self.atualizar()


    def preencher_letras(self, event):
        if event.char:
            teclaPressionada = event.char
            print(teclaPressionada)
            Partida.preencher_letras(teclaPressionada)
            self.atualizar()
            
    
    def passar_turno(self):
        Partida.passar_turno()
        self.atualizar()


    def __criaFrame(self, root, padx=0, pady=0, **kwargs):
        frame = Frame(root, **kwargs)
        frame.pack(padx=padx, pady=pady)
        frame.pack_propagate(0)
        return frame

    def __criaLabel(self, frame, padding=0, side='top', **kwargs):
        label = Label(frame, **kwargs)
        label.pack(pady=padding, side=side)
        return label
    
    def __fonte(self, tamanho):
        return ('Helvetica Neue', tamanho)