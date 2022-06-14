from tkinter import *
from turtle import bgcolor

from matplotlib.pyplot import text

from modules.jogador import Jogador

class InterfaceJogador:
    def __init__(self, partida):
        self.janela_principal = Tk()
        self.janela_principal.title("Wordle Versus")
        self.janela_principal.geometry("1200x900")
        self.janela_principal.resizable(False, False)
        self.janela_principal["bg"] = "gray"
        self.__partida = partida

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
                self.letras.append(letra)
            self.frames_tentativas.append(frames_tentativas)

        self.frame_instrucoes = self.__criaFrame(self.frame_mensagens, height=3*(3*height/10)/10, width=width, bg='gray')
        self.frame_mensagem = self.__criaFrame(self.frame_mensagens, height=2*(3*height/10)/10, width=width, bg='gray')
        self.frame_reset = self.__criaFrame(self.frame_mensagens, height=3*(3*height/10)/10, width=width, bg='gray')
        self.__criaLabel(self.frame_instrucoes, side='left', text="Pressione . para passar seu turno", font=self.__fonte(14))
        self.__criaLabel(self.frame_instrucoes, side='right', text="Pressione ENTER para submeter sua tentativa", font=self.__fonte(14))
        self.label_mensagem = self.__criaLabel(self.frame_mensagem, text='Jogador 1, é a sua vez!', font=self.__fonte(20))
        self.__criaLabel(self.frame_reset, text="Pressione CTRL para reiniciar o jogo", font=self.__fonte(14))
        
        self.janela_principal.bind('<Return>', lambda event: self.realizar_tentiva())
        self.janela_principal.bind('<Control_L>', lambda event: self.iniciar_partida())
        self.janela_principal.bind('.', lambda event: self.passar_turno())
        self.janela_principal.bind('<Key>', lambda event: self.preencher_letras(event))
        
        self.iniciar_partida()
        self.atualizar()
        self.janela_principal.mainloop()
        

    def atualizar(self):
        print (self.__partida.obter_palavra_secreta())
        tentativas = self.__partida.obter_tentativas()

        for i in range (len(self.letras)):
            indiceTentativa = int(i/5)
            indiceLetra = int(i%5)
            letra = ''
            imagemLetra = self.transparente
            corTentativa = 'grey'
            if len(tentativas) > indiceTentativa:
                corTentativa = self.pegarCorJogador(tentativas[indiceTentativa].obter_jogador())
                letrasTentativa = tentativas[indiceTentativa].obter_letras()
                letra  = letrasTentativa[indiceLetra].obter_letra()
                imagemLetra = self.pegarImagemDeCorLetra(letrasTentativa[indiceLetra].obter_cor())
            
            self.letras[i].configure(text=letra , image= imagemLetra)
            self.frames_tentativas[indiceTentativa].configure(bg = corTentativa)
            self.label_mensagem['text'] = self.contruirMensagem()

    def contruirMensagem(self) -> str:
        if (self.__partida.obter_em_andamento()):
            return f'Jogador {self.__partida.jogador_da_vez().obter_cor()} é sua vez!'
        else:
            if self.__partida.obter_vencedor():
                return f'Jogador {self.__partida.obter_vencedor().obter_cor()} venceu!'
            else:
                return f'Empate!'


    def pegarCorJogador(self, jogador):
        if jogador:
            corStr = jogador.obter_cor()
            if corStr == 'azul':
                return 'blue'
            else:
                return 'red'
        else:
            corStr = "grey"
        

    def pegarImagemDeCorLetra(self, cor):
        if cor == "verde":
            return self.imagens[1]
        elif cor == "amarelo":
            return self.imagens[2]
        elif cor == "cinza":
            return self.imagens[0]
        else:
            return self.transparente

    def iniciar_partida(self):
        self.__partida.iniciar_partida()
        self.atualizar()


    def realizar_tentiva(self):
        self.__partida.realizar_tentativa()
        self.atualizar()


    def preencher_letras(self, event):
        if event.char:
            teclaPressionada = event.char
            self.__partida.preencher_letras(teclaPressionada)
            self.atualizar()
            
    
    def passar_turno(self):
        self.__partida.passar_turno()
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