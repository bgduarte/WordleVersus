from tkinter import *
from turtle import bgcolor

from matplotlib.pyplot import text
from modules.partida import Partida
from modules.jogador import Jogador

class InterfaceJogador:
    def __init__(self, partida):
        self.janela_principal = Tk()
        self.janela_principal.title("Wordle Versus")
        self.janela_principal.geometry("1200x900")
        self.janela_principal.resizable(False, False)
        self.janela_principal["bg"] = "gray"
        self.__partida: Partida = partida

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
        
        self.labelsLetras = []
        self.frames_tentativas = []
        self.counter = 0
        for y in range(6):
            corJogador = 'grey'
            frames_tentativas = self.__criaFrame(self.frame_jogo, pady=3, height=(7*height/10)/6, width=6*width/10, bg=corJogador)
            for x in range(5):
                letra = Label(frames_tentativas, text=' ', font=self.__fonte(30), compound='center', relief='solid', image=self.transparente)
                letra.grid(row=0, column=x, padx=2, pady=8)
                self.labelsLetras.append(letra)
            self.frames_tentativas.append(frames_tentativas)

        self.frame_instrucoes = self.__criaFrame(self.frame_mensagens, height=3*(3*height/10)/10, width=width, bg='gray')
        self.frame_mensagem = self.__criaFrame(self.frame_mensagens, height=2*(3*height/10)/10, width=width, bg='gray')
        self.frame_reset = self.__criaFrame(self.frame_mensagens, height=3*(3*height/10)/10, width=width, bg='gray')
        self.label_passar_turno = self.__criaLabel(self.frame_instrucoes, side='left', text="Pressione . para passar seu turno", font=self.__fonte(14))
        self.__criaLabel(self.frame_instrucoes, side='right', text="Pressione ENTER para submeter sua tentativa", font=self.__fonte(14))
        self.label_mensagem = self.__criaLabel(self.frame_mensagem, text='Jogador 1, é a sua vez!', font=self.__fonte(20))
        self.__criaLabel(self.frame_reset, text="Pressione CTRL para reiniciar o jogo", font=self.__fonte(14))
        
        self.janela_principal.bind('<Return>', lambda event: self.realizar_tentiva())
        self.janela_principal.bind('<Control_L>', lambda event: self.iniciar_partida())
        self.janela_principal.bind('.', lambda event: self.passar_turno())
        self.janela_principal.bind('<Key>', lambda event: self.preencher_letras(event))
        
        self.iniciar_partida()
        self.atualizar_interface_grafica()
        self.janela_principal.mainloop()
        

    def atualizar_interface_grafica(self):
        print (self.__partida.obter_palavra_secreta())
        tentativas = self.__partida.obter_tentativas()
        
        for i in range (len(self.labelsLetras)):
            indiceTentativa = int(i/5)
            indiceLetra = int(i%5)

            if len(tentativas) > indiceTentativa:
                jogadorDaTentativa = tentativas[indiceTentativa].obter_jogador()
                corTentativa = self.traduzirCorJogador(jogadorDaTentativa)
                letras = tentativas[indiceTentativa].obter_letras()
                caracter  = letras[indiceLetra].obter_letra()
                imagemLetra = self.traduzirCorLetra(letras[indiceLetra].obter_cor())
            else:
                caracter = ''
                imagemLetra = self.transparente
                corTentativa = 'grey'   
          
            self.labelsLetras[i].configure(text=caracter , image= imagemLetra)
            self.frames_tentativas[indiceTentativa].configure(bg = corTentativa)
            self.atualizarMensagem();
        
        

    def atualizarMensagem(self):
        if (self.__partida.obter_em_andamento()):

            jogador = self.__partida.jogador_da_vez()
            cor = jogador.obter_cor()
            mensagem = f'Jogador {cor} é sua vez!'

            if jogador.pode_passar_turno():
                self.label_passar_turno.pack(side='left', pady=0)
            else:
                self.label_passar_turno.pack_forget()
        else:
            vencedor = self.__partida.obter_vencedor()
            if vencedor:
                mensagem = f'Jogador {vencedor.obter_cor()} venceu!'
            else:
                mensagem = f'Empate!'

        self.label_mensagem['text'] = mensagem


    def traduzirCorJogador(self, jogador):
        if jogador:
            corStr = jogador.obter_cor()
            if corStr == 'azul':
                return 'blue'
            else:
                return 'red'
        else:
            corStr = "grey"
        

    def traduzirCorLetra(self, cor):
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
        self.atualizar_interface_grafica()


    def realizar_tentiva(self):
        self.__partida.realizar_tentativa()
        self.atualizar_interface_grafica()


    def preencher_letras(self, event):
        if event.char:
            teclaPressionada = event.char
            self.__partida.preencher_letras(teclaPressionada)
            self.atualizar_interface_grafica()
            
    
    def passar_turno(self):
        self.__partida.passar_turno()
        self.atualizar_interface_grafica()


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